# Bundesliga — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,604 |
| Training data through | 2026-11-01 |
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
| Training sha256 | 0553d43788cf11198caa2b4132e71b88a246c7dc762d83855649a0387f0a145d |
| Training as of utc | 2026-11-06T13:18:36.199690+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 72, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 72, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 71, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-06T13:18:36.199690+00:00', 'observations': 420, 'observations_sha256': '00933fcfb924f085b453d0e96687f1a3345bb248107f4f29aaf4916330896265', 'eligible_training_matches': 84, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 116, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 22, 'retrospective_eligible_training_matches': 84, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': 'af0abbc63753fb14110ba2de2ff53217b3fda55e74d7baf3010d2bd9f2db8fdf', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-06', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1601, 'tune_start_date': '2025-11-07', 'audit_start_date': '2026-05-08', 'training_shot_matches': 1304, 'tuning_matches': 207, 'audit_matches': 82, 'audit_matchdays': 28, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.6694557879813141, 'audit_candidate_poisson_score': 0.6673643118188223, 'audit_gain': 0.0020914761624918343, 'audit_gain_lower95': -0.006070005754146365, 'audit_baseline_briers': [0.5838823503280925, 0.13631429107551435, 0.27437363687995375, 0.23545973809886073], 'audit_candidate_briers': [0.581834361341426, 0.13598518449839325, 0.27349907291047354, 0.23626015125232044], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1584.193 |
| Base scoring parameter | 0.218 |
| Home-advantage parameter | 0.226 |
| Dixon-Coles low-score adjustment | -0.079 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1604, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-01'} |
| Training data health | {'training_end': '2026-11-01', 'days_since_latest_result': 5, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261106T131836199690Z_bf5bc22d8b6eef86b33cc26c7c194881c501f6fea59c2a2166eb25069ddc47d8.json |
| Over 1 5 in window quote fixtures | 0 |
| Odds provider health | — |
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

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-06 — Hamburger SV vs Borussia Mönchengladbach

The model's most likely 1X2 outcome is **Hamburger SV win** at **37.6%**. Expected goals are 1.44 for Hamburger SV and 1.40 for Borussia Mönchengladbach (2.84 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 53.9%; Under 3.5 goals: 68.4%; Double Chance 1X: 64.5%; Double Chance X2: 62.4%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 84.2%; BTTS Yes (both teams score): 58.4%; BTTS No (at least one team does not score): 41.6%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 37.6% | 2.66 |
| Draw | 26.9% | 3.71 |
| Borussia Mönchengladbach win | 35.5% | 2.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.44 |
| Borussia Mönchengladbach expected goals | 1.40 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 53.9% |
| Under 2.5 | 46.1% |
| Over 3.5 | 31.6% |
| Under 3.5 | 68.4% |
| Over 4.5 | 15.8% |
| Under 4.5 | 84.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.71% |
| 2 | 2-1 | 8.50% |
| 3 | 1-2 | 8.22% |
| 4 | 1-0 | 7.52% |
| 5 | 0-1 | 7.25% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:30:00+00:00 |
| Fixture id | fdorg:565852 |
| Matched home-team name | Hamburg |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4420 |
| Dc lambda away | 1.3955 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-06T13:18:36.199690+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 58.4% |
| P btts no | 41.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.74 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.64 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.16 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.32 |
| Fair Under 4.5 odds | 1.19 |
| Score matrix json | [[0.06784229263319781,0.07247303604894194,0.05703235636352248,0.02652880497698119,0.009254976539381165,0.0025829913053020655,0.0006007438317893513,0.00011975920565723917,2.0889908906458353e-05,3.2390053337090716e-06,4.5199048205026364e-07,5.7339543475354936e-08,6.667923540766335e-09,7.157558155513359e-10,7.134351064384625e-11],[0.07519780051889936,0.12713379998641416,0.08223939645084351,0.038253950020281396,0.013345471470861986,0.0037246163323822108,0.00086625931835989,0.00017269012575786015,3.0122786606078936e-05,4.670574051814348e-06,6.517602781201953e-07,8.268235347182919e-08,9.614998266558142e-09,1.0321040551424899e-09,1.0287576439305072e-10],[0.06089803235246992,0.0849808140556084,0.05929369536732649,0.02758067491965687,0.009621937344829832,0.002685407185647877,0.0006245633886994848,0.00012450767091599734,2.1718196019390987e-05,3.367432240147225e-06,4.699119528008948e-07,5.961306248085877e-08,6.932307419296768e-09,7.441356098664978e-10,7.417228843901417e-11],[0.02927120524232972,0.04084681809561099,0.028500065759559733,0.01325690773755367,0.004624873611994921,0.0012907659222119014,0.00030020219753005043,5.984576921193071e-05,1.0439052767703396e-05,1.6185876034628532e-06,2.2586754752021266e-07,2.8653572530907402e-08,3.3320779906106573e-09,3.576756969495916e-10,3.565159980252806e-11],[0.010552107636822195,0.014725052063906015,0.010274116117244278,0.0047790419362641005,0.0016672413642160246,0.0004653139777594617,0.00010822123226298436,2.1574068887996738e-05,3.763220800760769e-06,5.834918811838693e-07,8.142400196257313e-08,1.0329454459510393e-08,1.201195691128003e-09,1.28940111008121e-10,1.2852204595837919e-11],[0.003043181164759423,0.004246639878331988,0.0029630096402205462,0.0013782545541218662,0.0004808250343263158,0.00013419449284951787,3.121052466338846e-05,6.221866033480476e-06,1.0852962321710078e-06,1.6827647743209946e-07,2.3482321983445868e-08,2.9789689733385657e-09,3.464195237807269e-10,3.71857576426383e-11,3.7065189531621415e-12],[0.0007313666552286582,0.0010205934630979597,0.0007120990610329586,0.0003312354305339106,0.0001155565107913129,3.2250915102261686e-05,7.500814376523812e-06,1.4952988678040629e-06,2.608288604197919e-07,4.044182642767663e-08,5.643498154140584e-09,7.159345619283281e-10,8.325488188063363e-11,8.936840009454347e-12,8.907863917888458e-13],[0.00015065922009729974,0.00021023902865610955,0.00014669015657229147,6.823345209418953e-05,2.3804276102171153e-05,6.643586608705671e-06,1.545144061439855e-06,3.080268421115022e-07,5.372992111245147e-08,8.33088846113609e-09,1.1625427881416689e-09,1.4748025763780723e-10,1.7150242609170542e-11,1.8409608044514764e-12,1.834991821143891e-13],[2.7155907892842554e-05,3.789500366442109e-05,2.6440495165786383e-05,1.2298891093978958e-05,4.290654955394522e-06,1.1974881186004954e-06,2.7850794519269786e-07,5.5520986684392325e-08,9.684669732639747e-09,1.5016196125935691e-09,2.0954512346389987e-10,2.6582908698441907e-11,3.091283814782513e-12,3.3182809527177193e-13,3.3075220253311294e-14],[4.350913172763386e-06,6.071528570359568e-06,4.236289913972186e-06,1.9705254371288857e-06,6.874477273554492e-07,1.918612645913332e-07,4.46224774454164e-08,8.895559422397825e-09,1.551675505745516e-09,2.4058914099628444e-10,3.3573270375088824e-11,4.259107376664125e-12,4.952847654205094e-13,5.316541934477045e-14,5.299304006334176e-15],[6.273920562870913e-07,8.755009910125067e-07,6.108636358898477e-07,2.8414540968214907e-07,9.912844180742245e-08,2.766597000080939e-08,6.434462552908921e-09,1.282719993765707e-09,2.2374817597697298e-10,3.469242200347918e-11,4.841191331688053e-12,6.141538635430136e-13,7.141896771695054e-14,7.666335879761074e-15,7.641479168642626e-16],[8.224413351707437e-08,1.1476846045085164e-07,8.007744109507915e-08,3.724830873770069e-08,1.2994638235614736e-08,3.626701530286426e-09,8.434866077901039e-10,1.6815035092508904e-10,2.933090190550862e-11,4.54779138290396e-12,6.346264385643728e-13,8.050875341358374e-14,9.362233802139007e-15,1.004971525162711e-15,1.0017130862846044e-16],[9.882851789948767e-09,1.3791131796177152e-08,9.622491577429311e-09,4.475936446026581e-09,1.5614984103385338e-09,4.3580194936043784e-10,1.0135741936980376e-10,2.0205757244381798e-11,3.5245426512699316e-12,5.464845489498055e-13,7.625977399363854e-14,9.674320146066066e-15,1.12501117262278e-15,1.2076222596764184e-16,1.20370676234891e-17],[1.0962195150011632e-09,1.529731309367416e-09,1.0673400020872945e-09,4.96477027514416e-10,1.7320355161020467e-10,4.833975169498492e-11,1.1242704379755936e-11,2.2412503877873372e-12,3.909471191003329e-13,6.061681789204398e-14,8.458839031303344e-15,1.0730888982138123e-15,1.2478778678819254e-16,1.339511222007261e-17,1.3351680985115563e-18],[1.1290887819727031e-10,1.5755990813914046e-10,1.0993433399205694e-10,5.1136349481343193e-11,1.7839692182519186e-11,4.9789180556683966e-12,1.1579807894775832e-12,2.308452491324211e-13,4.026693563471763e-14,6.243436478205414e-15,8.712470566396839e-16,1.1052646121077107e-16,1.2852944894855315e-17,1.3796753965772456e-18,1.3752020479909296e-19]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1874160560984655, "-10": 5.419756708429351e-07, "-11": 6.773432895158209e-08, "-12": 7.77419988434784e-09, "-13": 8.186315799443867e-10, "-14": 7.134351064384625e-11, "-2": 0.10631372212276761, "-3": 0.04288258682759645, "-4": 0.01366793932107661, "-5": 0.003584805054970755, "-6": 0.0007968552292699192, "-7": 0.00015348597704530802, "-8": 2.6060287755839665e-05, "-9": 3.953843398930698e-06, "0": 0.269335950352958, "1": 0.19397240047182066, "10": 7.522973250350692e-07, "11": 9.715374166482016e-08, "12": 1.152251743330824e-08, "13": 1.2537794231403036e-09, "14": 1.1290887819727031e-10, "2": 0.11351970884872499, "3": 0.04731555007629436, "4": 0.015583569150700253, "5": 0.004223479653310564, "6": 0.0009701195632699576, "7": 0.00019308810099910977, "8": 3.387715940397249e-05, "9": 5.3111457237866656e-06} |
| Raw goal margin distribution | {"-1": 0.1874160560984655, "-10": 5.419756708429351e-07, "-11": 6.773432895158209e-08, "-12": 7.77419988434784e-09, "-13": 8.186315799443867e-10, "-14": 7.134351064384625e-11, "-2": 0.10631372212276761, "-3": 0.04288258682759645, "-4": 0.01366793932107661, "-5": 0.003584805054970755, "-6": 0.0007968552292699192, "-7": 0.00015348597704530802, "-8": 2.6060287755839665e-05, "-9": 3.953843398930698e-06, "0": 0.269335950352958, "1": 0.19397240047182066, "10": 7.522973250350692e-07, "11": 9.715374166482016e-08, "12": 1.152251743330824e-08, "13": 1.2537794231403036e-09, "14": 1.1290887819727031e-10, "2": 0.11351970884872499, "3": 0.04731555007629436, "4": 0.015583569150700253, "5": 0.004223479653310564, "6": 0.0009701195632699576, "7": 0.00019308810099910977, "8": 3.387715940397249e-05, "9": 5.3111457237866656e-06} |
| Research history json | {"away": [{"away": "Paderborn", "away_goals": 0.0, "away_xg": 0.99, "date": "2026-10-31T00:00:00+00:00", "home": "M'gladbach", "home_goals": 0.0, "home_xg": 1.32, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 3.0, "away_xg": 2.6, "date": "2026-10-23T00:00:00+00:00", "home": "Stuttgart", "home_goals": 2.0, "home_xg": 1.55, "source": "pipeline training history"}, {"away": "Hoffenheim", "away_goals": 2.0, "away_xg": 1.8, "date": "2026-10-18T00:00:00+00:00", "home": "M'gladbach", "home_goals": 1.0, "home_xg": 0.47, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 1.0, "away_xg": 1.17, "date": "2026-10-11T00:00:00+00:00", "home": "FC Koln", "home_goals": 2.0, "home_xg": 1.32, "source": "pipeline training history"}, {"away": "Mainz", "away_goals": 4.0, "away_xg": 2.82, "date": "2026-09-19T00:00:00+00:00", "home": "M'gladbach", "home_goals": 3.0, "home_xg": 3.24, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 0.0, "away_xg": 0.19, "date": "2026-09-12T00:00:00+00:00", "home": "Freiburg", "home_goals": 5.0, "home_xg": 2.6, "source": "pipeline training history"}, {"away": "Elversberg", "away_goals": 4.0, "away_xg": 2.31, "date": "2026-09-05T00:00:00+00:00", "home": "M'gladbach", "home_goals": 3.0, "home_xg": 2.37, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 0.0, "away_xg": 1.09, "date": "2026-08-29T00:00:00+00:00", "home": "RB Leipzig", "home_goals": 3.0, "home_xg": 3.96, "source": "pipeline training history"}, {"away": "Hoffenheim", "away_goals": 0.0, "away_xg": null, "date": "2026-05-16T00:00:00+00:00", "home": "M'gladbach", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 1.0, "away_xg": null, "date": "2026-05-09T00:00:00+00:00", "home": "Augsburg", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 37.6% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 58.4% |
| P home draw | 64.5% |
| P draw away | 62.4% |
| P home away | 73.1% |
| Raw p home draw | 64.5% |
| Raw p draw away | 62.4% |
| Raw p home away | 73.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5394 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Count model | {"corners": {"alpha": 0.011823964613419384, "mu": 9.857583967086907, "version": "count-markets-nb2-v1"}} |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-01 |
| Elo home rating | 1,426.8279 |
| Elo away rating | 1,410.3288 |
| Elo rating diff | 76.4991 |
| Elo home expectancy | 0.6083 |
| Research p home | 0.3851 |
| Research p draw | 0.2508 |
| Research p away | 0.3641 |
| Research p over 1 5 | 0.7752 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4419778822858402, 1.3954607525535545], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:21:37.670067+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ger.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-06T13:21:37.764946+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ger.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:21:37.969483+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22Hamburger+SV%22+%22Borussia+M%C3%B6nchengladbach%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:21:38.128219+00:00", "reason": null, "status": "available", "url": "https://understat.com/league/Bundesliga/2026"}, {"observed_at_utc": "2026-11-06T13:21:38.286500+00:00", "reason": null, "status": "available", "url": "https://understat.com/league/Bundesliga/2025"}, {"observed_at_utc": "2026-11-06T13:21:28.744830+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:21:29.042627+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:21:38.392862+00:00", "reason": "HTTPError", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Hamburger+SV_vs_Borussia+M%C3%B6nchengladbach&d=2026-11-06"}]}, "form": {"away": {"all": {"goals_against": 2.2633171886423034, "goals_for": 1.4955413906153532, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 0.7941779248780608, "results": "DWLLLLLLWL", "xg_against": 1.9317425773677326, "xg_for": 1.5670287632962654, "xg_matches": 8}, "venue": {"goals_against": 2.908133877985406, "goals_for": 1.1507795353021404, "last_match": "2026-10-23T00:00:00+00:00", "matches": 5, "points_per_game": 0.7766966202232553, "results": "WLLLL", "xg_against": 2.2146664815541426, "xg_for": 1.362970544404023, "xg_matches": 4}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.4419778822858402, 1.3954607525535545], "h2h": [], "margin_distribution": {"-1": 0.19668284148005669, "-10": 5.41975670842935e-07, "-11": 6.773432895158209e-08, "-12": 7.774199884347839e-09, "-13": 8.186315799443865e-10, "-14": 7.134351064384623e-11, "-2": 0.1063137221227676, "-3": 0.04288258682759644, "-4": 0.013667939321076608, "-5": 0.003584805054970755, "-6": 0.0007968552292699191, "-7": 0.00015348597704530802, "-8": 2.6060287755839665e-05, "-9": 3.953843398930697e-06, "0": 0.2508023795897755, "1": 0.20323918585341186, "10": 7.522973250350691e-07, "11": 9.715374166482016e-08, "12": 1.1522517433308239e-08, "13": 1.2537794231403036e-09, "14": 1.1290887819727031e-10, "2": 0.11351970884872498, "3": 0.04731555007629435, "4": 0.015583569150700253, "5": 0.004223479653310564, "6": 0.0009701195632699575, "7": 0.00019308810099910974, "8": 3.387715940397249e-05, "9": 5.311145723786665e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:21:38.393439+00:00", "p_over_1_5": 0.7752200854173695, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
