# Ligue 1 — football model report

Fixtures in this report: **13**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,743 |
| Training data through | 2026-10-18 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | e6ab17eecfcf978f021b8e3d8997dc88783763687971fad5382c1c763b9521fe |
| Training as of utc | 2026-10-21T17:26:41.937526+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 63, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 63, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 21, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T17:26:41.937526+00:00', 'observations': 125, 'observations_sha256': '1105eb92dcf68011c1b8768d6ed3bffc7538110ab15fe942e65ff790508667d2', 'eligible_training_matches': 35, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 65, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 35, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '734cc3ce0de75f01ee3b4d42cdbebbb029c6e85b73a5c9ce7f4c507b9e812675', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 5079.453 |
| Base scoring parameter | 0.216 |
| Home-advantage parameter | 0.187 |
| Dixon-Coles low-score adjustment | -0.057 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 13.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261021T172641937526Z_ac3ffe484999d41470c0fcdc8be70e3a67d4ca8601c075b75a0679fe1e9c5faa.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **39.1%**. Expected goals are 1.22 for Brest and 1.24 for Nice (2.46 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 44.7%; Under 3.5 goals: 76.6%; Double Chance 1X: 67.4%; Double Chance X2: 60.9%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 50.7%; BTTS No (at least one team does not score): 49.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 39.1% | 2.56 |
| Draw | 28.4% | 3.53 |
| Nice win | 32.6% | 3.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.22 |
| Nice expected goals | 1.24 |
| Expected total goals | 2.46 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 71.1% |
| Under 1.5 | 28.9% |
| Over 2.5 | 44.7% |
| Under 2.5 | 55.3% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.48% |
| 2 | 1-0 | 10.78% |
| 3 | 0-0 | 9.17% |
| 4 | 0-1 | 8.90% |
| 5 | 2-1 | 8.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 39.1% | 43.0% | 2.30 | -10.2% |
| Draw | 28.4% | 28.0% | 3.36 | -4.7% |
| Nice win | 32.6% | 29.0% | 3.32 | +8.2% |
| Over 2.5 | 44.7% | 56.2% | 1.76 | -21.4% |
| Under 2.5 | 55.3% | 43.8% | 2.23 | +23.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:45:00+00:00 |
| Fixture id | 8aa36b30d655d6c81ed98bf9ec1b4039 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brest |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2187 |
| Dc lambda away | 1.2397 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:26:41.937526+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.91 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.47 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.64 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.18197614798583064, "-10": 2.0907722217591556e-07, "-11": 2.329956270582748e-08, "-12": 2.383779007222936e-09, "-13": 2.2437774301857186e-10, "-14": 1.7933993039903656e-11, "-2": 0.09541278429182849, "-3": 0.035285188752654684, "-4": 0.010201289219074138, "-5": 0.002412038414107637, "-6": 0.00048151023792421125, "-7": 8.308234940763961e-05, "-8": 1.261471591034973e-05, "-9": 1.709358390129578e-06, "0": 0.28356657774503086, "1": 0.22043807713383046, "10": 2.1716779508738093e-07, "11": 2.3789518163033694e-08, "12": 2.3925060338117723e-09, "13": 2.2136859122191253e-10, "14": 1.7392515459914794e-11, "2": 0.11368466039811723, "3": 0.04132728921468596, "4": 0.011744883416748557, "5": 0.0027297762122100878, "6": 0.0005356702479220282, "7": 9.085523251786454e-05, "8": 1.3560254007785693e-05, "9": 1.8062283453110792e-06} |
| Raw goal margin distribution | {"-1": 0.20179382189258943, "-10": 2.3184627326461027e-07, "-11": 2.58369454396906e-08, "-12": 2.6433787160518075e-09, "-13": 2.4881306046150844e-10, "-14": 1.9887051338173412e-11, "-2": 0.10580348365853122, "-3": 0.03912783721058879, "-4": 0.011312236040455842, "-5": 0.002674715645549434, "-6": 0.0005339479501385112, "-7": 9.213023247468967e-05, "-8": 1.3988491150153013e-05, "-9": 1.89551194673749e-06, "0": 0.2874155266300256, "1": 0.19823624513008603, "10": 1.9529533563825224e-07, "11": 2.1393512479382948e-08, "12": 2.1515403271549075e-09, "13": 1.9907304075659684e-10, "14": 1.5640795832415403e-11, "2": 0.10223469783094521, "3": 0.037164934215746424, "4": 0.010561975581983215, "5": 0.0024548417106062138, "6": 0.00048171922000343184, "7": 8.170457835117025e-05, "8": 1.2194507738704505e-05, "9": 1.6243106893216758e-06} |
| Unadjusted home-win probability | 35.1% |
| Unadjusted draw probability | 28.7% |
| Unadjusted away-win probability | 36.1% |
| Raw p over 1 5 | 71.1% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 50.8% |
| P home draw | 67.4% |
| P draw away | 60.9% |
| P home away | 71.6% |
| Raw p home draw | 63.9% |
| Raw p draw away | 64.9% |
| Raw p home away | 71.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.67, "price": 2.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.41, "price": 1.67, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.25 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.28 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.16 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | -3.9% |
| Draw probability edge | +0.4% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -11.6% |
| Under 2.5 probability edge | +11.6% |
| Raw edge prob home | -0.0787 |
| Raw ev home | -0.1922 |
| Raw edge prob draw | 0.0077 |
| Raw ev draw | -0.0343 |
| Raw edge prob away | 0.0710 |
| Raw ev away | 0.1997 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **46.6%**. Expected goals are 1.68 for RC Lens and 1.03 for Paris FC (2.70 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.8%; Double Chance 1X: 72.2%; Double Chance X2: 53.4%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 86.4%; BTTS Yes (both teams score): 53.0%; BTTS No (at least one team does not score): 47.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 46.6% | 2.14 |
| Draw | 25.6% | 3.91 |
| Paris FC win | 27.8% | 3.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.68 |
| Paris FC expected goals | 1.03 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.21% |
| 2 | 1-0 | 9.50% |
| 3 | 2-1 | 8.68% |
| 4 | 2-0 | 8.46% |
| 5 | 0-1 | 7.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 46.6% | 41.3% | 2.40 | +11.9% |
| Draw | 25.6% | 25.6% | 3.67 | -6.0% |
| Paris FC win | 27.8% | 33.0% | 2.90 | -19.5% |
| Over 2.5 | 50.4% | 58.1% | 1.71 | -13.8% |
| Under 2.5 | 49.6% | 41.9% | 2.32 | +15.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | fc6c50376190b578cfeb38c029db8487 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lens |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6772 |
| Dc lambda away | 1.0253 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:26:41.937526+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.0% |
| P btts no | 47.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.56 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.07 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.54 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.38 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.17401389511510967, "-10": 3.421483301753063e-08, "-11": 3.1484701520939714e-09, "-12": 2.6609505753026457e-10, "-13": 2.0786657535142102e-11, "-14": 1.501764624548915e-12, "-15": 9.209055284938408e-14, "-2": 0.07450432742345235, "-3": 0.022483303780435126, "-4": 0.005328654009108907, "-5": 0.0010355736578708111, "-6": 0.00017019216425588995, "-7": 2.4201455984927586e-05, "-8": 3.030588295022406e-06, "-9": 3.388654709277372e-07, "0": 0.2560217513244935, "1": 0.21051312207863324, "10": 3.410634814214719e-06, "11": 5.134124981172698e-07, "12": 7.098224389819304e-08, "13": 9.070759185932121e-09, "14": 1.0720299192787427e-09, "15": 1.0753904529798605e-10, "2": 0.1448217576073932, "3": 0.07149217403396763, "4": 0.027718004302719573, "5": 0.008811939165574604, "6": 0.0023690603094421578, "7": 0.0005510920045474728, "8": 0.00011289003752415366, "9": 2.0649144057787646e-05} |
| Raw goal margin distribution | {"-1": 0.14085795655972314, "-10": 2.769567027790206e-08, "-11": 2.5485727540313496e-09, "-12": 2.1539432830671974e-10, "-13": 1.682604772549943e-11, "-14": 1.2156241667236395e-12, "-15": 7.45439729639906e-14, "-2": 0.06030855931810469, "-3": 0.01819942151819922, "-4": 0.004313352760941007, "-5": 0.0008382594345024489, "-6": 0.00013776440360526031, "-7": 1.9590203607315145e-05, "-8": 2.453151652793531e-06, "-9": 2.74299346911089e-07, "0": 0.2555544025641058, "1": 0.23459374722584084, "10": 3.8007778022819555e-06, "11": 5.721418247786043e-07, "12": 7.910191259410254e-08, "13": 1.0108364583639498e-08, "14": 1.194659569999993e-09, "15": 1.198404515615922e-10, "2": 0.16138793848803568, "3": 0.0796701737086285, "4": 0.03088867064813228, "5": 0.009819938105360112, "6": 0.0026400574458652973, "7": 0.0006141314951601956, "8": 0.00012580354452851949, "9": 2.3011202502203943e-05} |
| Unadjusted home-win probability | 52.0% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 22.5% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 52.8% |
| P home draw | 72.2% |
| P draw away | 53.4% |
| P home away | 74.4% |
| Raw p home draw | 77.5% |
| Raw p draw away | 48.0% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.1, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.34 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | +5.3% |
| Draw probability edge | -0.0% |
| Away probability edge | -5.3% |
| Over 2.5 probability edge | -7.7% |
| Under 2.5 probability edge | +7.7% |
| Raw edge prob home | 0.1067 |
| Raw ev home | 0.2474 |
| Raw edge prob draw | -0.0009 |
| Raw ev draw | -0.0621 |
| Raw edge prob away | -0.1058 |
| Raw ev away | -0.3484 |

</details>


---

## 2026-10-24 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **59.8%**. Expected goals are 1.91 for Toulouse and 0.91 for Troyes (2.82 combined). The most likely exact score is 2-0 at 10.8%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.6%; Under 3.5 goals: 68.8%; Double Chance 1X: 82.4%; Double Chance X2: 40.2%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 84.5%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 59.8% | 1.67 |
| Draw | 22.6% | 4.42 |
| Troyes win | 17.6% | 5.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.91 |
| Troyes expected goals | 0.91 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 53.6% |
| Under 2.5 | 46.4% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.5% |
| Under 4.5 | 84.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.79% |
| 2 | 1-1 | 10.79% |
| 3 | 1-0 | 10.73% |
| 4 | 2-1 | 9.83% |
| 5 | 3-0 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 59.8% | 59.4% | 1.65 | -1.4% |
| Draw | 22.6% | 22.3% | 4.23 | -4.3% |
| Troyes win | 17.6% | 18.4% | 5.09 | -10.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T15:15:00+00:00 |
| Fixture id | 0bbce95e5764e706e6c428bb52dc5536 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 0.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9077 |
| Dc lambda away | 0.9104 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:26:41.937526+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.48 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.49 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.21 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.44 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.11657973572702336, "-10": 7.87444636104257e-09, "-11": 6.433620954894322e-10, "-12": 4.827854252879606e-11, "-13": 3.3493498832396785e-12, "-14": 2.1599424078434808e-13, "-15": 1.2951780776503906e-14, "-16": 6.648112822704345e-16, "-2": 0.044511737392395875, "-3": 0.011914806769278577, "-4": 0.002505756365503096, "-5": 0.0004322040986165558, "-6": 6.305087387469499e-05, "-7": 7.959289524718205e-06, "-8": 8.848445486322873e-07, "-9": 8.784018277932032e-08, "0": 0.2263435659886696, "1": 0.23851987298752805, "10": 1.2206105344163681e-05, "11": 2.089626418856113e-06, "12": 3.285666094005123e-07, "13": 4.776237215915697e-08, "14": 6.4539208848120274e-09, "15": 8.108995251489582e-10, "16": 8.72151711938752e-11, "2": 0.18568758525134416, "3": 0.10414811673949788, "4": 0.045894363946533234, "5": 0.016586910042846202, "6": 0.005070185090160229, "7": 0.0013411059880632777, "8": 0.00031240061042383366, "9": 6.498217153904155e-05} |
| Raw goal margin distribution | {"-1": 0.11151305011071581, "-10": 7.53221412089321e-09, "-11": 6.154008597312166e-10, "-12": 4.618030310938517e-11, "-13": 3.2037833937330622e-12, "-14": 2.0660688966228126e-13, "-15": 1.2388881907702732e-14, "-16": 6.359178408808791e-16, "-2": 0.04257720753438528, "-3": 0.011396975949861183, "-4": 0.002396853393164974, "-5": 0.0004134200254145262, "-6": 6.031061242390077e-05, "-7": 7.6133699058459735e-06, "-8": 8.463882155546326e-07, "-9": 8.402255025642684e-08, "0": 0.2299803339762986, "1": 0.24012151007670657, "10": 1.2288068120634952e-05, "11": 2.103658051244003e-06, "12": 3.307729013177857e-07, "13": 4.8083091710777944e-08, "14": 6.497258318000578e-09, "15": 8.163446343501681e-10, "16": 8.780081234475098e-11, "2": 0.18693445881291995, "3": 0.1048474609259959, "4": 0.04620254000985382, "5": 0.01669828948467946, "6": 0.005104230875895764, "7": 0.0013501113806290946, "8": 0.0003144983492749816, "9": 6.541852032108928e-05} |
| Unadjusted home-win probability | 60.2% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.8% |
| Raw p btts yes | 51.5% |
| P home draw | 82.4% |
| P draw away | 40.2% |
| P home away | 77.4% |
| Raw p home draw | 83.2% |
| Raw p draw away | 39.8% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.65 |
| Reference draw odds | 4.23 |
| Reference away odds | 5.09 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:29Z |
| Market reference home last update utc | 2026-10-21T17:28:29Z |
| Market reference draw last update utc | 2026-10-21T17:28:29Z |
| Market reference away last update utc | 2026-10-21T17:28:29Z |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Home probability edge | +0.4% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.8% |
| Raw edge prob home | 0.0080 |
| Raw ev home | -0.0073 |
| Raw edge prob draw | 0.0073 |
| Raw ev draw | -0.0272 |
| Raw edge prob away | -0.0153 |
| Raw ev away | -0.1430 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **44.2%**. Expected goals are 1.56 for AS Monaco and 1.26 for Lille (2.82 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 53.2%; Under 3.5 goals: 68.7%; Double Chance 1X: 71.5%; Double Chance X2: 55.8%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 57.6%; BTTS No (at least one team does not score): 42.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 44.2% | 2.26 |
| Draw | 27.3% | 3.66 |
| Lille win | 28.5% | 3.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.56 |
| Lille expected goals | 1.26 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 77.9% |
| Under 1.5 | 22.1% |
| Over 2.5 | 53.2% |
| Under 2.5 | 46.8% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.4% |
| Under 4.5 | 84.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.92% |
| 2 | 2-1 | 9.27% |
| 3 | 1-0 | 8.73% |
| 4 | 2-0 | 7.33% |
| 5 | 1-2 | 6.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 44.2% | 44.9% | 2.16 | -4.6% |
| Draw | 27.3% | 28.5% | 3.22 | -12.0% |
| Lille win | 28.5% | 26.7% | 3.83 | +9.0% |
| Over 2.5 | 53.2% | 53.2% | 1.86 | -1.1% |
| Under 2.5 | 46.8% | 46.8% | 2.03 | -5.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | c177a3c900d7febf9870ca8de90a9e35 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Monaco |
| Matched away-team name | Lille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5579 |
| Dc lambda away | 1.2641 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:26:41.937526+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.6% |
| P btts no | 42.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.48 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.53 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.48 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.16103056467521618, "-10": 1.9176025177789531e-07, "-11": 2.1716304637742132e-08, "-12": 2.2593395676088472e-09, "-13": 2.1728914953032932e-10, "-14": 1.9301724476711215e-11, "-15": 1.4378194770933846e-12, "-2": 0.08226264492934326, "-3": 0.030135799188084445, "-4": 0.008715959472973368, "-5": 0.0020733262482508594, "-6": 0.00041786246380931335, "-7": 7.295967321200343e-05, "-8": 1.1227680575357908e-05, "-9": 1.543764931759303e-06, "0": 0.27342103781917143, "1": 0.21590378079826034, "10": 1.6744972627870643e-06, "11": 2.3371356544713954e-07, "12": 2.996757828763171e-08, "13": 3.552060263809091e-09, "14": 3.888754637972573e-10, "15": 3.570186778618762e-11, "2": 0.1349433106765734, "3": 0.060926123996456534, "4": 0.021717417671983364, "5": 0.006366969542444668, "6": 0.0015815052281409417, "7": 0.00034032377995905265, "8": 6.454633825764545e-05, "9": 1.0937923387301562e-05} |
| Raw goal margin distribution | {"-1": 0.17128557566070055, "-10": 2.039722408032572e-07, "-11": 2.309927775885946e-08, "-12": 2.403222513883668e-09, "-13": 2.3112691144810164e-10, "-14": 2.053092836695833e-11, "-15": 1.5293850414474254e-12, "-2": 0.0875014288157867, "-3": 0.03205495628943019, "-4": 0.009271023415800956, "-5": 0.0022053631910212528, "-6": 0.0004444734625686414, "-7": 7.760601008473004e-05, "-8": 1.1942700036874615e-05, "-9": 1.6420774873050622e-06, "0": 0.2619449700414192, "1": 0.21265143664081146, "10": 1.649272871768277e-06, "11": 2.3019293720113016e-07, "12": 2.951615090735927e-08, "13": 3.4985525280798094e-09, "14": 3.830174985593162e-10, "15": 3.5164059876223694e-11, "2": 0.1329105436428369, "3": 0.06000834144219438, "4": 0.021390269549707762, "5": 0.006271058409645309, "6": 0.0015576816560399728, "7": 0.00033519719045099305, "8": 6.357402130543269e-05, "9": 1.0773156049315227e-05} |
| Unadjusted home-win probability | 43.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 30.3% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.3% |
| P home draw | 71.5% |
| P draw away | 55.8% |
| P home away | 72.7% |
| Raw p home draw | 69.7% |
| Raw p draw away | 56.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.59, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.6, "price": 1.59, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.16 |
| Reference draw odds | 3.34 |
| Reference away odds | 3.56 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 2.03 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:29Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:29Z |
| Home probability edge | -0.7% |
| Draw probability edge | -1.1% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0133 |
| Raw ev home | -0.0600 |
| Raw edge prob draw | -0.0230 |
| Raw ev draw | -0.1565 |
| Raw edge prob away | 0.0363 |
| Raw ev away | 0.1599 |

</details>


---

## 2026-10-25 — Angers vs Lorient

The model's most likely 1X2 outcome is **Lorient win** at **38.9%**. Expected goals are 1.19 for Angers and 1.30 for Lorient (2.49 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 45.3%; Under 3.5 goals: 76.0%; Double Chance 1X: 61.1%; Double Chance X2: 67.6%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 89.3%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 32.4% | 3.08 |
| Draw | 28.7% | 3.49 |
| Lorient win | 38.9% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 1.19 |
| Lorient expected goals | 1.30 |
| Expected total goals | 2.49 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 24.0% |
| Under 3.5 | 76.0% |
| Over 4.5 | 10.7% |
| Under 4.5 | 89.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.66% |
| 2 | 0-1 | 10.18% |
| 3 | 0-0 | 9.09% |
| 4 | 1-0 | 8.94% |
| 5 | 1-2 | 8.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 32.4% | 31.7% | 3.04 | -1.4% |
| Draw | 28.7% | 28.9% | 3.35 | -3.9% |
| Lorient win | 38.9% | 39.4% | 2.47 | -4.0% |
| Over 2.5 | 45.3% | 47.1% | 2.08 | -5.8% |
| Under 2.5 | 54.7% | 52.9% | 1.87 | +2.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 1a83b5ebabe7cb572ae6e029b3149c42 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Angers |
| Matched away-team name | Lorient |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1904 |
| Dc lambda away | 1.2991 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:26:41.937526+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.00 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.16 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.33 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.21109318191676338, "-10": 3.647667419921238e-07, "-11": 4.258403646119693e-08, "-12": 4.564227215523892e-09, "-13": 4.499948324685488e-10, "-14": 3.7602333173433415e-11, "-2": 0.11537023014951113, "-3": 0.04460478435955257, "-4": 0.013492536807703598, "-5": 0.003339405081534244, "-6": 0.0006980036474311535, "-7": 0.00012612681323693862, "-8": 2.0057514680873e-05, "-9": 2.846903745254357e-06, "0": 0.2869439499568324, "1": 0.18601382724999663, "10": 1.4683977675195767e-07, "11": 1.5707819161709706e-08, "12": 1.5426837695408454e-09, "13": 1.393662989840884e-10, "14": 1.0671012287916912e-11, "2": 0.09345392568983615, "3": 0.03310745678770619, "4": 0.009176531814490782, "5": 0.00208110816528457, "6": 0.0003985876405430306, "7": 6.599547288081467e-05, "8": 9.616663668441691e-06, "9": 1.2507216822497396e-06} |
| Raw goal margin distribution | {"-1": 0.20826178215888977, "-10": 3.5987411374340995e-07, "-11": 4.2012855386418975e-08, "-12": 4.503007086500443e-09, "-13": 4.4395903705286254e-10, "-14": 3.7097971847899346e-11, "-2": 0.11382276547658789, "-3": 0.04400649892707734, "-4": 0.013311560969907488, "-5": 0.003294613531880943, "-6": 0.0006886413016633456, "-7": 0.0001244350701630138, "-8": 1.978848258000029e-05, "-9": 2.8087181321435492e-06, "0": 0.2848235416547979, "1": 0.190220791769588, "10": 1.5016076498166585e-07, "11": 1.606307360096523e-08, "12": 1.577573734331933e-09, "13": 1.4251826399508106e-10, "14": 1.0912352250365275e-11, "2": 0.0955675177566521, "3": 0.03385622852203858, "4": 0.009384071997536313, "5": 0.002128175355623154, "6": 0.0004076022610500242, "7": 6.748805338930615e-05, "8": 9.834158052854334e-06, "9": 1.2790085134971645e-06} |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 38.4% |
| Raw p over 1 5 | 71.8% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 51.3% |
| P home draw | 61.1% |
| P draw away | 67.6% |
| P home away | 71.3% |
| Raw p home draw | 61.6% |
| Raw p draw away | 66.8% |
| Raw p home away | 71.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.12, "price": 1.81, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.02 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | +0.7% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | 0.0147 |
| Raw ev home | 0.0082 |
| Raw edge prob draw | -0.0042 |
| Raw ev draw | -0.0458 |
| Raw edge prob away | -0.0104 |
| Raw ev away | -0.0527 |

</details>


---

## 2026-10-25 — Auxerre vs Le Mans FC

The model's most likely 1X2 outcome is **Auxerre win** at **43.5%**. Expected goals are 1.73 for Auxerre and 1.52 for Le Mans FC (3.24 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 62.6%; Under 3.5 goals: 59.3%; Double Chance 1X: 68.8%; Double Chance X2: 56.5%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 77.4%; BTTS Yes (both teams score): 65.0%; BTTS No (at least one team does not score): 35.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 43.5% | 2.30 |
| Draw | 25.3% | 3.95 |
| Le Mans FC win | 31.2% | 3.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Auxerre expected goals | 1.73 |
| Le Mans FC expected goals | 1.52 |
| Expected total goals | 3.24 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 84.0% |
| Under 1.5 | 16.0% |
| Over 2.5 | 62.6% |
| Under 2.5 | 37.4% |
| Over 3.5 | 40.7% |
| Under 3.5 | 59.3% |
| Over 4.5 | 22.6% |
| Under 4.5 | 77.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.26% |
| 2 | 2-1 | 9.07% |
| 3 | 1-2 | 7.24% |
| 4 | 2-2 | 6.98% |
| 5 | 1-0 | 6.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 43.5% | 44.6% | 2.13 | -7.4% |
| Draw | 25.3% | 26.3% | 3.77 | -4.6% |
| Le Mans FC win | 31.2% | 29.0% | 3.35 | +4.5% |
| Over 2.5 | 62.6% | 55.6% | 1.78 | +11.4% |
| Under 2.5 | 37.4% | 44.4% | 2.20 | -17.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 8eab078a37a63df32ffa443302a2a7ba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Auxerre |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7277 |
| Dc lambda away | 1.5164 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:26:41.937526+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 65.0% |
| P btts no | 35.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.40 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.26 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.46 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.43 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.1617885439311625, "-10": 8.175400102888536e-07, "-11": 1.1054027196691889e-07, "-12": 1.3740676392686918e-08, "-13": 1.5802372640530904e-09, "-14": 1.6896749208660244e-10, "-15": 1.6718762818314833e-11, "-16": 1.3615403393364713e-12, "-2": 0.09285096947201976, "-3": 0.03928167436566257, "-4": 0.01328370371928326, "-5": 0.0037218548645894505, "-6": 0.0008876363591864731, "-7": 0.00018396956590759653, "-8": 3.367889612723325e-05, "-9": 5.517419956001101e-06, "0": 0.2531101828403149, "1": 0.20336562285646254, "10": 3.3117262075533847e-06, "11": 5.101902847308513e-07, "12": 7.225801286209203e-08, "13": 9.468178742345635e-09, "14": 1.1534892571392632e-09, "15": 1.3004114344538609e-10, "16": 1.206628010495939e-11, "2": 0.13243472580638285, "3": 0.06383688281286923, "4": 0.02459614860125322, "5": 0.007851879177614051, "6": 0.0021336122924871317, "7": 0.000503840009908166, "8": 0.00010509226772354178, "9": 1.961621456541037e-05} |
| Raw goal margin distribution | {"-1": 0.17308018198309627, "-10": 8.74598227544852e-07, "-11": 1.1825516148186403e-07, "-12": 1.4699673492512394e-08, "-13": 1.6905260817178168e-09, "-14": 1.8076016737019158e-10, "-15": 1.7885608219314684e-11, "-16": 1.456565736879055e-12, "-2": 0.0993312771290025, "-3": 0.04202324331877528, "-4": 0.014210807522449275, "-5": 0.003981612675566809, "-6": 0.0009495867806819187, "-7": 0.00019680927445756528, "-8": 3.60294327957578e-05, "-9": 5.9024948668068264e-06, "0": 0.24277712465226492, "1": 0.19801321606136832, "10": 3.224564446347995e-06, "11": 4.967625189736472e-07, "12": 7.035624463985889e-08, "13": 9.218984490505607e-09, "14": 1.1231304204230988e-09, "15": 1.2661857334704566e-10, "16": 1.1748706078837588e-11, "2": 0.12894915869648427, "3": 0.06215675142907877, "4": 0.02394879930466431, "5": 0.007645224528346298, "6": 0.00207745746763522, "7": 0.0004905793778760934, "8": 0.00010232633039365019, "9": 1.9099932813070965e-05} |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 84.0% |
| Raw p under 3 5 | 59.3% |
| Raw p btts yes | 64.8% |
| P home draw | 68.8% |
| P draw away | 56.5% |
| P home away | 74.7% |
| Raw p home draw | 66.6% |
| Raw p draw away | 57.7% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.65, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.45, "price": 1.65, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.17 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.28 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | -1.1% |
| Draw probability edge | -1.0% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | +7.0% |
| Under 2.5 probability edge | -7.0% |
| Raw edge prob home | -0.0229 |
| Raw ev home | -0.0981 |
| Raw edge prob draw | -0.0207 |
| Raw ev draw | -0.0847 |
| Raw edge prob away | 0.0436 |
| Raw ev away | 0.1183 |

</details>


---

## 2026-10-25 — Marseille vs Le Havre

The model's most likely 1X2 outcome is **Marseille win** at **64.6%**. Expected goals are 2.11 for Marseille and 0.81 for Le Havre (2.92 combined). The most likely exact score is 2-0 at 11.6%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 55.7%; Under 3.5 goals: 66.8%; Double Chance 1X: 84.9%; Double Chance X2: 35.4%; Double Chance 12 (either team wins): 79.7%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 49.5%; BTTS No (at least one team does not score): 50.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 64.6% | 1.55 |
| Draw | 20.3% | 4.92 |
| Le Havre win | 15.1% | 6.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 2.11 |
| Le Havre expected goals | 0.81 |
| Expected total goals | 2.92 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 55.7% |
| Under 2.5 | 44.3% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.0% |
| Under 4.5 | 83.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.59% |
| 2 | 1-0 | 10.47% |
| 3 | 1-1 | 9.68% |
| 4 | 2-1 | 9.39% |
| 5 | 3-0 | 8.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 64.6% | 62.3% | 1.58 | +2.1% |
| Draw | 20.3% | 20.2% | 4.91 | -0.3% |
| Le Havre win | 15.1% | 17.4% | 4.95 | -25.5% |
| Over 2.5 | 55.7% | 60.5% | 1.65 | -8.1% |
| Under 2.5 | 44.3% | 39.5% | 2.45 | +8.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | fcc34b753fc61a0cc0e11d7cb0a0c36b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Marseille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1127 |
| Dc lambda away | 0.8100 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:26:41.937526+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 49.5% |
| P btts no | 50.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.02 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.79 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.87 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.1043745667359873, "-10": 2.49745700351366e-09, "-11": 1.815734893316513e-10, "-12": 1.2124337603030023e-11, "-13": 7.48452223421964e-13, "-14": 4.2955183699398434e-14, "-15": 2.3028887664293233e-15, "-16": 1.1535918109805325e-16, "-17": 4.99379744279665e-18, "-2": 0.03577521699066348, "-3": 0.008533606363087696, "-4": 0.00159839276471264, "-5": 0.0002454684456041838, "-6": 3.1876833613781185e-05, "-7": 3.5816222041866588e-06, "-8": 3.5436862809730494e-07, "-9": 3.130665250520924e-08, "0": 0.20312456024273906, "1": 0.2295671002071868, "10": 2.9599271515045926e-05, "11": 5.612853734516627e-06, "12": 9.775468698408367e-07, "13": 1.5739536337507723e-07, "14": 2.3560891289041003e-08, "15": 3.2945596805810287e-09, "16": 4.304521342004345e-10, "17": 4.860174994578744e-11, "2": 0.19796071525307626, "3": 0.12316225352920204, "4": 0.06016955629057064, "5": 0.02410112190786624, "6": 0.008163286627618125, "7": 0.002392312595994854, "8": 0.0006173645719900747, "9": 0.00014225624866588636} |
| Raw goal margin distribution | {"-1": 0.08789936057079117, "-10": 2.1032410531310484e-09, "-11": 1.5291266932135308e-10, "-12": 1.0210547990550727e-11, "-13": 6.303113288411319e-13, "-14": 3.617483931625422e-14, "-15": 1.93938481724976e-15, "-16": 9.715008714850849e-17, "-17": 4.2055417882806076e-18, "-2": 0.03012820839500923, "-3": 0.007186602695804215, "-4": 0.0013460913549428696, "-5": 0.00020672200214723788, "-6": 2.6845172912289397e-05, "-7": 3.0162740924279916e-06, "-8": 2.984326238679545e-07, "-9": 2.636499314800072e-08, "0": 0.20403768769548852, "1": 0.2376843061354984, "10": 3.064586478559207e-05, "11": 5.8113172319753e-06, "12": 1.0121117061780695e-06, "13": 1.629606668332987e-07, "14": 2.4393974976882617e-08, "15": 3.41105119589944e-09, "16": 4.456723840203465e-10, "17": 5.032024711907671e-11, "2": 0.20496035888657094, "3": 0.12751711698127854, "4": 0.062297076647733776, "5": 0.024953307475628052, "6": 0.008451930246622786, "7": 0.002476901781331334, "8": 0.0006391938121519476, "9": 0.00014728625193712145} |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 66.5% |
| Raw p btts yes | 49.3% |
| P home draw | 84.9% |
| P draw away | 35.4% |
| P home away | 79.7% |
| Raw p home draw | 87.3% |
| Raw p draw away | 33.1% |
| Raw p home away | 79.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.62, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.58, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.57 |
| Reference draw odds | 4.60 |
| Reference away odds | 5.30 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | +2.3% |
| Draw probability edge | +0.1% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -4.7% |
| Under 2.5 probability edge | +4.7% |
| Raw edge prob home | 0.0457 |
| Raw ev home | 0.0573 |
| Raw edge prob draw | 0.0018 |
| Raw ev draw | 0.0018 |
| Raw edge prob away | -0.0475 |
| Raw ev away | -0.3724 |

</details>


---

## 2026-10-25 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **67.4%**. Expected goals are 2.42 for Paris Saint Germain and 1.10 for Lyon (3.52 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 68.5%; Under 3.5 goals: 53.1%; Double Chance 1X: 85.7%; Double Chance X2: 32.6%; Double Chance 12 (either team wins): 81.7%; Under 4.5 goals: 72.0%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 67.4% | 1.48 |
| Draw | 18.3% | 5.46 |
| Lyon win | 14.3% | 7.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 2.42 |
| Lyon expected goals | 1.10 |
| Expected total goals | 3.52 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 87.2% |
| Under 1.5 | 12.8% |
| Over 2.5 | 68.5% |
| Under 2.5 | 31.5% |
| Over 3.5 | 46.9% |
| Under 3.5 | 53.1% |
| Over 4.5 | 28.0% |
| Under 4.5 | 72.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.71% |
| 2 | 2-0 | 8.86% |
| 3 | 1-1 | 8.11% |
| 4 | 3-1 | 7.84% |
| 5 | 3-0 | 7.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 67.4% | 68.6% | 1.46 | -1.6% |
| Draw | 18.3% | 17.8% | 5.35 | -2.1% |
| Lyon win | 14.3% | 13.5% | 6.06 | -13.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T19:45:00+00:00 |
| Fixture id | 8664b2167f22c59026d86615421463b1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4237 |
| Dc lambda away | 1.0958 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:26:41.937526+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.09 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.79 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.18 |
| Fair Over 3.5 odds | 2.13 |
| Fair Under 3.5 odds | 1.88 |
| Fair Over 4.5 odds | 3.57 |
| Fair Under 4.5 odds | 1.39 |
| Goal margin distribution | {"-1": 0.09013589243874791, "-10": 2.455253079272294e-08, "-11": 2.3983909596895345e-09, "-12": 2.1539560675686701e-10, "-13": 1.7898032383734436e-11, "-14": 1.3835792935433687e-12, "-15": 9.997629544596466e-14, "-16": 6.778307276851982e-15, "-17": 4.2935704053426747e-16, "-18": 2.277725025290386e-17, "-2": 0.037752414758813885, "-3": 0.011518555910944207, "-4": 0.0028109555893585264, "-5": 0.0005685764687887613, "-6": 9.791899660973261e-05, "-7": 1.4657265176388467e-05, "-8": 1.9381658529798483e-06, "-9": 2.2936774513478499e-07, "0": 0.18301860794705727, "1": 0.2195265078916668, "10": 7.386146610066142e-05, "11": 1.5958684881214033e-05, "12": 3.1700741676288186e-06, "13": 5.826306572438263e-07, "14": 9.96202342120078e-08, "15": 1.5921940849404937e-08, "16": 2.387677570757988e-09, "17": 3.345249213917555e-10, "18": 3.925243862648784e-11, "2": 0.1982543406798016, "3": 0.1337924064170529, "4": 0.07221757080340327, "5": 0.03230972301628142, "6": 0.012307412840366613, "7": 0.00407481804451544, "8": 0.0011917953172641724, "9": 0.00031195973540988154} |
| Raw goal margin distribution | {"-1": 0.09497930247660133, "-10": 2.5871849555523117e-08, "-11": 2.527267376559219e-09, "-12": 2.2696978897938926e-10, "-13": 1.8859774785787127e-11, "-14": 1.4579252800000725e-12, "-15": 1.0534847493860615e-13, "-16": 7.14253644922823e-15, "-17": 4.524283403647969e-16, "-18": 2.4001175145915614e-17, "-2": 0.03978102311502782, "-3": 0.01213750012740664, "-4": 0.002962000973712056, "-5": 0.0005991286595055738, "-6": 0.00010318062811128341, "-7": 1.5444866467750186e-05, "-8": 2.0423122889151937e-06, "-9": 2.416927136804789e-07, "0": 0.18769783242738908, "1": 0.21550191570533364, "10": 7.250735956384845e-05, "11": 1.566611338680124e-05, "12": 3.1119570142715047e-06, "13": 5.719492556528221e-07, "14": 9.779389068720586e-08, "15": 1.5630042985455877e-08, "16": 2.3439041395352874e-09, "17": 3.2839205662887516e-10, "18": 3.8532821395257413e-11, "2": 0.19461973236725874, "3": 0.13133958247962432, "4": 0.07089360189430564, "5": 0.031717386992523945, "6": 0.012081780327796606, "7": 0.004000114169251415, "8": 0.0011699460646721485, "9": 0.00030624055950880663} |
| Unadjusted home-win probability | 66.2% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 15.1% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 53.2% |
| Raw p btts yes | 61.1% |
| P home draw | 85.7% |
| P draw away | 32.6% |
| P home away | 81.7% |
| Raw p home draw | 84.9% |
| Raw p draw away | 33.8% |
| Raw p home away | 81.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.43 |
| Reference draw odds | 5.15 |
| Reference away odds | 6.70 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.05 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:31Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:31Z |
| Home probability edge | -1.2% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -1.5% |
| Under 2.5 probability edge | +1.5% |
| Raw edge prob home | -0.0247 |
| Raw ev home | -0.0339 |
| Raw edge prob draw | 0.0094 |
| Raw ev draw | 0.0042 |
| Raw edge prob away | 0.0154 |
| Raw ev away | -0.0875 |

</details>


---

## 2026-10-25 — Rennes vs Strasbourg

The model's most likely 1X2 outcome is **Rennes win** at **54.1%**. Expected goals are 1.90 for Rennes and 1.25 for Strasbourg (3.16 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 61.4%; Under 3.5 goals: 61.1%; Double Chance 1X: 76.7%; Double Chance X2: 45.9%; Double Chance 12 (either team wins): 77.3%; Under 4.5 goals: 78.7%; BTTS Yes (both teams score): 61.1%; BTTS No (at least one team does not score): 38.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 54.1% | 1.85 |
| Draw | 22.7% | 4.41 |
| Strasbourg win | 23.3% | 4.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.90 |
| Strasbourg expected goals | 1.25 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 61.4% |
| Under 2.5 | 38.6% |
| Over 3.5 | 38.9% |
| Under 3.5 | 61.1% |
| Over 4.5 | 21.3% |
| Under 4.5 | 78.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.35% |
| 2 | 2-1 | 10.04% |
| 3 | 2-0 | 8.02% |
| 4 | 1-0 | 7.83% |
| 5 | 3-1 | 6.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 54.1% | 56.1% | 1.77 | -4.3% |
| Draw | 22.7% | 21.8% | 4.45 | +0.8% |
| Strasbourg win | 23.3% | 22.1% | 4.06 | -5.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 31dcb6d13ed240fc4a5c7a696149967e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Rennes |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9036 |
| Dc lambda away | 1.2515 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:26:41.937526+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.1% |
| P btts no | 38.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.42 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.59 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.69 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.13514285723245334, "-10": 1.3063918316008776e-07, "-11": 1.4604019810674059e-08, "-12": 1.5005061473034905e-09, "-13": 1.426086672820359e-10, "-14": 1.2601113328131279e-11, "-15": 1.03185350928177e-12, "-16": 7.025240931231456e-14, "-2": 0.06583243424156465, "-3": 0.02329959248189374, "-4": 0.0065630670460294985, "-5": 0.0015277367556431442, "-6": 0.000302207450228686, "-7": 5.189350095460555e-05, "-8": 7.864707400509809e-06, "-9": 1.0660374801451258e-06, "0": 0.22653887617679808, "1": 0.22755178136469398, "10": 9.451197704939174e-06, "11": 1.6069857728691846e-06, "12": 2.5113290710356456e-07, "13": 3.6302621948385296e-08, "14": 4.878959529876625e-09, "15": 6.076626880889279e-10, "16": 6.292626785301048e-11, "2": 0.16628133123556268, "3": 0.08951135481723815, "4": 0.038349779648934136, "5": 0.013577843106718583, "6": 0.004085203092090062, "7": 0.0010669588816189862, "8": 0.0002459481205966237, "9": 5.070603352411755e-05} |
| Raw goal margin distribution | {"-1": 0.1420335014968549, "-10": 1.373001947487342e-07, "-11": 1.534864743958778e-08, "-12": 1.5770137355649374e-09, "-13": 1.4987997717872298e-10, "-14": 1.3243617053875433e-11, "-15": 1.0844655052913348e-12, "-16": 7.383442889663959e-14, "-2": 0.06918908878260312, "-3": 0.024487588700014995, "-4": 0.006897703749912548, "-5": 0.0016056327741850683, "-6": 0.00031761635955784016, "-7": 5.453943920125303e-05, "-8": 8.265711952657943e-06, "-9": 1.1203924434678569e-06, "0": 0.23489506125297288, "1": 0.21904170492701516, "10": 9.09773787081139e-06, "11": 1.5468870486167848e-06, "12": 2.417409338891574e-07, "13": 3.4944961349922284e-08, "14": 4.696494166228043e-09, "15": 5.849370654067031e-10, "16": 6.057292503954017e-11, "2": 0.1600626726494287, "3": 0.08616377183209754, "4": 0.03691555859285935, "5": 0.013070053266516023, "6": 0.003932422962799794, "7": 0.001027056308305857, "8": 0.00023675005019072235, "9": 4.8809708131480144e-05} |
| Unadjusted home-win probability | 52.1% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 61.3% |
| Raw p btts yes | 61.3% |
| P home draw | 76.7% |
| P draw away | 45.9% |
| P home away | 77.3% |
| Raw p home draw | 75.5% |
| Raw p draw away | 47.9% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.74 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.25 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.86 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:31Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:31Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.8% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | -0.0404 |
| Raw ev home | -0.0787 |
| Raw edge prob draw | 0.0167 |
| Raw ev draw | 0.0453 |
| Raw edge prob away | 0.0237 |
| Raw ev away | -0.0069 |

</details>


---

## 2026-10-25 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **59.7%**. Expected goals are 1.91 for Toulouse and 0.91 for Troyes (2.82 combined). The most likely exact score is 2-0 at 10.8%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.6%; Under 3.5 goals: 68.9%; Double Chance 1X: 82.1%; Double Chance X2: 40.3%; Double Chance 12 (either team wins): 77.5%; Under 4.5 goals: 84.5%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 59.7% | 1.68 |
| Draw | 22.5% | 4.45 |
| Troyes win | 17.9% | 5.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.91 |
| Troyes expected goals | 0.91 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 53.6% |
| Under 2.5 | 46.4% |
| Over 3.5 | 31.1% |
| Under 3.5 | 68.9% |
| Over 4.5 | 15.5% |
| Under 4.5 | 84.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.78% |
| 2 | 1-1 | 10.71% |
| 3 | 1-0 | 10.71% |
| 4 | 2-1 | 9.81% |
| 5 | 3-0 | 6.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 59.7% | 59.2% | 1.71 | +2.0% |
| Draw | 22.5% | 22.0% | 4.26 | -4.2% |
| Troyes win | 17.9% | 18.9% | 5.13 | -8.4% |
| Over 2.5 | 53.6% | 60.0% | 1.67 | -10.5% |
| Under 2.5 | 46.4% | 40.0% | 2.40 | +11.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 18e4425261f7dd6b245f82056d424411 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:09Z |
| Market best draw last update utc | 2026-10-21T17:28:09Z |
| Market best away last update utc | 2026-10-21T17:28:09Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9077 |
| Dc lambda away | 0.9104 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:26:41.937526+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.59 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.49 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.21 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.43 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.11826869883674831, "-10": 7.988528361060572e-09, "-11": 6.526828821484563e-10, "-12": 4.89779837894398e-11, "-13": 3.397873997306976e-12, "-14": 2.1912348363537002e-13, "-15": 1.3139421276804758e-14, "-16": 6.744428166334295e-16, "-2": 0.04515660660518562, "-3": 0.012087423982444449, "-4": 0.002542058815812324, "-5": 0.00043846570809682225, "-6": 6.396433108358444e-05, "-7": 8.074600700395825e-06, "-8": 8.976638417209293e-07, "-9": 8.911277811795753e-08, "0": 0.22476617410158967, "1": 0.23813167979349528, "10": 1.2186239800211716e-05, "11": 2.0862255334552e-06, "12": 3.2803186434988765e-07, "13": 4.768463847780449e-08, "14": 6.4434170717295805e-09, "15": 8.095797790298427e-10, "16": 8.70732277346162e-11, "2": 0.18538537707091846, "3": 0.10397861476222775, "4": 0.04581967046499915, "5": 0.01655991470066353, "6": 0.005061933319270726, "7": 0.0013389233262560162, "8": 0.00031189217567892434, "9": 6.487641248253625e-05} |
| Raw goal margin distribution | {"-1": 0.11151305011071581, "-10": 7.53221412089321e-09, "-11": 6.154008597312166e-10, "-12": 4.618030310938517e-11, "-13": 3.2037833937330622e-12, "-14": 2.0660688966228126e-13, "-15": 1.2388881907702732e-14, "-16": 6.359178408808791e-16, "-2": 0.04257720753438528, "-3": 0.011396975949861183, "-4": 0.002396853393164974, "-5": 0.0004134200254145262, "-6": 6.031061242390077e-05, "-7": 7.6133699058459735e-06, "-8": 8.463882155546326e-07, "-9": 8.402255025642684e-08, "0": 0.2299803339762986, "1": 0.24012151007670657, "10": 1.2288068120634952e-05, "11": 2.103658051244003e-06, "12": 3.307729013177857e-07, "13": 4.8083091710777944e-08, "14": 6.497258318000578e-09, "15": 8.163446343501681e-10, "16": 8.780081234475098e-11, "2": 0.18693445881291995, "3": 0.1048474609259959, "4": 0.04620254000985382, "5": 0.01669828948467946, "6": 0.005104230875895764, "7": 0.0013501113806290946, "8": 0.0003144983492749816, "9": 6.541852032108928e-05} |
| Unadjusted home-win probability | 60.2% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.8% |
| Raw p btts yes | 51.5% |
| P home draw | 82.1% |
| P draw away | 40.3% |
| P home away | 77.5% |
| Raw p home draw | 83.2% |
| Raw p draw away | 39.8% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.74, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.54, "price": 2.74, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.67 |
| Reference draw odds | 4.40 |
| Reference away odds | 5.10 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | +0.5% |
| Draw probability edge | +0.5% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | 0.0100 |
| Raw ev home | 0.0288 |
| Raw edge prob draw | 0.0104 |
| Raw ev draw | -0.0203 |
| Raw edge prob away | -0.0204 |
| Raw ev away | -0.1363 |

</details>


---

## 2026-10-30 — Le Havre vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **74.6%**. Expected goals are 0.82 for Le Havre and 2.31 for Paris Saint Germain (3.13 combined). The most likely exact score is 0-2 at 12.4%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 61.8%; Under 3.5 goals: 61.1%; Double Chance 1X: 25.4%; Double Chance X2: 90.3%; Double Chance 12 (either team wins): 84.2%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 49.9%; BTTS No (at least one team does not score): 50.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 9.7% | 10.33 |
| Draw | 15.8% | 6.34 |
| Paris Saint Germain win | 74.6% | 1.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 0.82 |
| Paris Saint Germain expected goals | 2.31 |
| Expected total goals | 3.13 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 61.8% |
| Under 2.5 | 38.2% |
| Over 3.5 | 38.9% |
| Under 3.5 | 61.1% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.36% |
| 2 | 0-1 | 10.22% |
| 3 | 1-2 | 10.15% |
| 4 | 0-3 | 9.51% |
| 5 | 1-3 | 7.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 9.7% | 8.1% | 9.70 | -6.1% |
| Draw | 15.8% | 13.0% | 6.87 | +8.3% |
| Paris Saint Germain win | 74.6% | 78.8% | 1.23 | -8.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T18:00:00+00:00 |
| Fixture id | 9a9f6c78276f74f15f42b013b033aa5d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Le Havre |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8210 |
| Dc lambda away | 2.3072 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:26:41.937526+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 49.9% |
| P btts no | 50.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.17 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.62 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.68 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.24129092520137332, "-10": 6.491345559579036e-05, "-11": 1.3424854672791416e-05, "-12": 2.550482647433199e-06, "-13": 4.480272814820618e-07, "-14": 7.317945756901466e-08, "-15": 1.1168305161013763e-08, "-16": 1.5991118658435865e-09, "-17": 2.146850768436546e-10, "-18": 2.4897633109888078e-11, "-2": 0.22271428420546627, "-3": 0.14960246294810356, "-4": 0.07921566369170181, "-5": 0.03446779541586064, "-6": 0.012699469984497338, "-7": 0.004052100300823991, "-8": 0.0011392540348133318, "-9": 0.0002861306588219114, "0": 0.15761417502101802, "1": 0.06720386206770546, "10": 1.7184256591404344e-09, "11": 1.2646296669868213e-10, "12": 8.549365779449655e-12, "13": 5.344089688936644e-13, "14": 3.106105602367511e-14, "15": 1.686832871931295e-15, "16": 8.594515165594942e-17, "17": 4.105841178120728e-18, "18": 1.6944006321544297e-19, "2": 0.022934119452218578, "3": 0.0054818922405625616, "4": 0.0010329054493493522, "5": 0.00015992662149428785, "6": 2.096769085929013e-05, "7": 2.3806905525656456e-06, "8": 2.381776959899333e-07, "9": 2.1286421720172576e-08} |
| Raw goal margin distribution | {"-1": 0.22749593744280341, "-10": 6.120224961254395e-05, "-11": 1.265733427923671e-05, "-12": 2.4046674789993972e-06, "-13": 4.2241284588572783e-07, "-14": 6.899567104450761e-08, "-15": 1.0529795308844313e-08, "-16": 1.5076880852124424e-09, "-17": 2.0241118794984632e-10, "-18": 2.3474195640444798e-11, "-2": 0.20998135269671186, "-3": 0.14104945108784128, "-4": 0.07468677761775597, "-5": 0.032497216474983076, "-6": 0.011973420992682745, "-7": 0.0038204352516734135, "-8": 0.001074121061200523, "-9": 0.00026977211184172283, "0": 0.18480766883440786, "1": 0.0779127253781033, "10": 1.9922549440448566e-09, "11": 1.4661470474670082e-10, "12": 9.91169804289133e-12, "13": 6.195664646632868e-13, "14": 3.601060197237423e-14, "15": 1.9556278800931654e-15, "16": 9.964041935273343e-17, "17": 4.7601025642654805e-18, "18": 1.9644015547876105e-19, "2": 0.02658864677850101, "3": 0.006355425886997525, "4": 0.0011974978243902905, "5": 0.00018541075702731204, "6": 2.4308869899277454e-05, "7": 2.760051037623725e-06, "8": 2.7613105628003147e-07, "9": 2.467839018084166e-08} |
| Unadjusted home-win probability | 11.2% |
| Unadjusted draw probability | 18.5% |
| Unadjusted away-win probability | 70.3% |
| Raw p over 1 5 | 82.4% |
| Raw p under 3 5 | 61.9% |
| Raw p btts yes | 50.9% |
| P home draw | 25.4% |
| P draw away | 90.3% |
| P home away | 84.2% |
| Raw p home draw | 29.7% |
| Raw p draw away | 88.8% |
| Raw p home away | 81.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -2.0, "market_key": "spreads", "opposite_price": 1.8, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.26, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.75, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 2.0, "market_key": "spreads", "opposite_price": 2.05, "price": 1.8, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 10.50 |
| Reference draw odds | 6.75 |
| Reference away odds | 1.25 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.37 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:31Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:31Z |
| Home probability edge | +1.5% |
| Draw probability edge | +2.7% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -11.5% |
| Under 2.5 probability edge | +11.5% |
| Raw edge prob home | 0.0309 |
| Raw ev home | 0.0890 |
| Raw edge prob draw | 0.0544 |
| Raw ev draw | 0.2696 |
| Raw edge prob away | -0.0852 |
| Raw ev away | -0.1354 |

</details>


---

## 2026-10-30 — Lille vs RC Lens

The model's most likely 1X2 outcome is **Lille win** at **39.4%**. Expected goals are 1.25 for Lille and 1.12 for RC Lens (2.37 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 42.7%; Under 3.5 goals: 78.4%; Double Chance 1X: 67.4%; Double Chance X2: 60.6%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 90.7%; BTTS Yes (both teams score): 48.5%; BTTS No (at least one team does not score): 51.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 39.4% | 2.54 |
| Draw | 28.0% | 3.57 |
| RC Lens win | 32.6% | 3.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.25 |
| RC Lens expected goals | 1.12 |
| Expected total goals | 2.37 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 69.3% |
| Under 1.5 | 30.7% |
| Over 2.5 | 42.7% |
| Under 2.5 | 57.3% |
| Over 3.5 | 21.6% |
| Under 3.5 | 78.4% |
| Over 4.5 | 9.3% |
| Under 4.5 | 90.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.22% |
| 2 | 1-0 | 11.22% |
| 3 | 0-1 | 9.82% |
| 4 | 0-0 | 9.64% |
| 5 | 2-1 | 8.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 39.4% | 40.6% | 2.31 | -8.9% |
| Draw | 28.0% | 26.7% | 3.50 | -2.1% |
| RC Lens win | 32.6% | 32.8% | 3.02 | -1.6% |
| Over 2.5 | 42.7% | 56.6% | 1.75 | -25.3% |
| Under 2.5 | 57.3% | 43.4% | 2.25 | +29.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:05:00+00:00 |
| Fixture id | 7932d9a82dcdb164a3e4ef5e03694ee3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2460 |
| Dc lambda away | 1.1238 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:26:41.937526+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.5% |
| P btts no | 51.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.37 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.26 |
| Fair Over 2.5 odds | 2.34 |
| Fair Under 2.5 odds | 1.74 |
| Fair Over 3.5 odds | 4.64 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.71 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.19169623544981224, "-10": 9.455309655307655e-08, "-11": 9.559485527514202e-09, "-12": 8.872227176360825e-10, "-13": 7.579686774646149e-11, "-14": 5.531172968971885e-12, "-2": 0.09247251359992019, "-3": 0.03122567631765622, "-4": 0.00822220438407377, "-5": 0.0017681218090772864, "-6": 0.00032073690429442077, "-7": 5.025968274112673e-05, "-8": 6.927645909402737e-06, "-9": 8.51955174404004e-07, "0": 0.279810560737368, "1": 0.21818100363252255, "10": 2.714972272765583e-07, "11": 3.043427015339036e-08, "12": 3.131841349995789e-09, "13": 2.966586993931268e-10, "14": 2.4002794009460353e-11, "2": 0.11624986931516466, "3": 0.04352415948642974, "4": 0.012707073341490493, "5": 0.0030297596574499243, "6": 0.0006093736340769434, "7": 0.00010587494512178393, "8": 1.6180720868826143e-05, "9": 2.206315714881443e-06} |
| Raw goal margin distribution | {"-1": 0.1905078370507524, "-10": 9.396692568589097e-08, "-11": 9.500222614655863e-09, "-12": 8.817224841298053e-10, "-13": 7.532697392683441e-11, "-14": 5.496883108840697e-12, "-2": 0.09189924106349649, "-3": 0.031032096388147492, "-4": 0.008171231789312854, "-5": 0.0017571605446459857, "-6": 0.00031874853335594875, "-7": 4.994810371420083e-05, "-8": 6.884698778549227e-06, "-9": 8.466735779086073e-07, "0": 0.29293523686489487, "1": 0.21203807101353814, "10": 2.638531650271701e-07, "11": 2.957738679623461e-08, "12": 3.0436636898600947e-09, "13": 2.8830621053815345e-10, "14": 2.332699023272175e-11, "2": 0.11297682948915135, "3": 0.04229872750760637, "4": 0.012349302985585715, "5": 0.0029444561291061865, "6": 0.0005922165896432073, "7": 0.00010289401349577852, "8": 1.5725149227074934e-05, "9": 2.1441964260933567e-06} |
| Unadjusted home-win probability | 38.3% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 69.2% |
| Raw p under 3 5 | 78.5% |
| Raw p btts yes | 48.8% |
| P home draw | 67.4% |
| P draw away | 60.6% |
| P home away | 72.0% |
| Raw p home draw | 67.6% |
| Raw p draw away | 61.7% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.38 |
| Reference draw odds | 3.56 |
| Reference away odds | 2.92 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.18 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | -1.1% |
| Draw probability edge | +1.3% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -13.9% |
| Under 2.5 probability edge | +13.9% |
| Raw edge prob home | -0.0222 |
| Raw ev home | -0.1145 |
| Raw edge prob draw | 0.0262 |
| Raw ev draw | 0.0253 |
| Raw edge prob away | -0.0040 |
| Raw ev away | -0.0223 |

</details>


---

## 2026-10-31 — Nice vs Rennes

The model's most likely 1X2 outcome is **Rennes win** at **37.2%**. Expected goals are 1.34 for Nice and 1.30 for Rennes (2.64 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 49.6%; Under 3.5 goals: 72.7%; Double Chance 1X: 62.8%; Double Chance X2: 63.6%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 54.2%; BTTS No (at least one team does not score): 45.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nice win | 36.4% | 2.75 |
| Draw | 26.5% | 3.78 |
| Rennes win | 37.2% | 2.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nice expected goals | 1.34 |
| Rennes expected goals | 1.30 |
| Expected total goals | 2.64 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 74.8% |
| Under 1.5 | 25.2% |
| Over 2.5 | 49.6% |
| Under 2.5 | 50.4% |
| Over 3.5 | 27.3% |
| Under 3.5 | 72.7% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.61% |
| 2 | 0-1 | 9.03% |
| 3 | 1-0 | 8.65% |
| 4 | 1-2 | 8.53% |
| 5 | 2-1 | 8.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nice win | 36.4% | 35.4% | 2.78 | +1.1% |
| Draw | 26.5% | 25.4% | 3.79 | +0.3% |
| Rennes win | 37.2% | 39.2% | 2.35 | -12.6% |
| Over 2.5 | 49.6% | 60.5% | 1.65 | -18.2% |
| Under 2.5 | 50.4% | 39.5% | 2.45 | +23.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T16:15:00+00:00 |
| Fixture id | a547720e6b4661d6319c4f11dbdf8e1f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nice |
| Matched away-team name | Rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3431 |
| Dc lambda away | 1.2984 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:26:41.937526+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 54.2% |
| P btts no | 45.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.30 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.97 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.66 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.71 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.20432309048473685, "-10": 3.3075826767719357e-07, "-11": 3.853611563995304e-08, "-12": 4.1226290602877114e-09, "-13": 4.0527608805697707e-10, "-14": 3.342195939322686e-11, "-2": 0.10944717104937814, "-3": 0.041761085910731174, "-4": 0.012521157015844515, "-5": 0.0030793088904471676, "-6": 0.0006405274588676238, "-7": 0.00011529718368111317, "-8": 1.8277627851628413e-05, "-9": 2.587391908613996e-06, "0": 0.2645381565815692, "1": 0.19530565293776653, "10": 4.284773881383917e-07, "11": 5.16431606938567e-08, "12": 5.715402448214822e-09, "13": 5.81234273242535e-10, "14": 4.9586084982246095e-11, "2": 0.1080936824451654, "3": 0.042667307053817334, "4": 0.013234135906563428, "5": 0.0033669143058923947, "6": 0.0007245097558912811, "7": 0.00013491270906472366, "8": 2.2124918159158526e-05, "9": 3.240050181524649e-06} |
| Raw goal margin distribution | {"-1": 0.1932790409899815, "-10": 3.128801577173242e-07, "-11": 3.6453165702902005e-08, "-12": 3.8997931620917845e-09, "-13": 3.8337014896353715e-10, "-14": 3.1615439274160465e-11, "-2": 0.10353134444719302, "-3": 0.039503820230877465, "-4": 0.011844364796783404, "-5": 0.00291286642075342, "-6": 0.0006059057382304629, "-7": 0.00010906515283154442, "-8": 1.7289687496178567e-05, "-9": 2.44753848219376e-06, "0": 0.2755491082015514, "1": 0.20018969232492467, "10": 4.3919239002746355e-07, "11": 5.293460939035963e-08, "12": 5.8583284221979524e-09, "13": 5.957692907444982e-10, "14": 5.0826092060717254e-11, "2": 0.11079679827731892, "3": 0.04373429515713259, "4": 0.01356508403863442, "5": 0.0034511112650475123, "6": 0.0007426276860736751, "7": 0.00013828649254200108, "8": 2.2678199490761423e-05, "9": 3.3210746294343962e-06} |
| Unadjusted home-win probability | 37.3% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 35.2% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.7% |
| Raw p btts yes | 54.4% |
| P home draw | 62.8% |
| P draw away | 63.6% |
| P home away | 73.5% |
| Raw p home draw | 64.8% |
| Raw p draw away | 62.7% |
| Raw p home away | 72.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.89, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.11, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.71 |
| Reference draw odds | 3.74 |
| Reference away odds | 2.46 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | +0.9% |
| Draw probability edge | +1.1% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -10.9% |
| Under 2.5 probability edge | +10.9% |
| Raw edge prob home | 0.0182 |
| Raw ev home | 0.0360 |
| Raw edge prob draw | 0.0220 |
| Raw ev draw | 0.0443 |
| Raw edge prob away | -0.0402 |
| Raw ev away | -0.1733 |

</details>


---
