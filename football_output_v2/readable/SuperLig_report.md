# Super Lig — football model report

Fixtures in this report: **6**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Super Lig |
| Training matches | 1,840 |
| Training data through | 2026-11-02 |
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
| Training sha256 | 428b36b889bc8107b0a0c389334f72426054f163962dc5b037f54c55da735d9c |
| Training as of utc | 2026-11-05T12:31:25.260459+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1809, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1512, 'tuning_matches': 189, 'audit_matches': 91, 'audit_matchdays': 37, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8325677188807528, 'audit_candidate_poisson_score': 0.8249863531892144, 'audit_gain': 0.007581365691538333, 'audit_gain_lower95': -0.0033666616245295734, 'audit_baseline_briers': [0.5922611421709056, 0.1664906883092837, 0.22016705451566723, 0.2497257630051956], 'audit_candidate_briers': [0.5911071175486112, 0.16507678151874086, 0.21632127980415214, 0.24937363636848253], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1672.176 |
| Base scoring parameter | 0.131 |
| Home-advantage parameter | 0.246 |
| Dixon-Coles low-score adjustment | -0.097 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1840, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 6.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 7.00 |
| Over 1 5 in window quote fixtures | 2 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 2.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 2.00 |
| Totals anchor fixtures | {'ANCHORED_MAIN': 3, 'ANCHORED_ALTERNATE': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 6} |
| Legacy comparison status | {'None': 6} |
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

## 2026-11-06 — Gazişehir Gaziantep vs Kasimpasa SK

The model's most likely 1X2 outcome is **Gazişehir Gaziantep win** at **36.9%**. Expected goals are 1.39 for Gazişehir Gaziantep and 1.41 for Kasimpasa SK (2.81 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 51.0%; Under 3.5 goals: 71.2%; Double Chance 1X: 64.7%; Double Chance X2: 63.1%; Double Chance 12 (either team wins): 72.2%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 56.2%; BTTS No (at least one team does not score): 43.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Gazişehir Gaziantep win | 36.9% | 2.71 |
| Draw | 27.8% | 3.59 |
| Kasimpasa SK win | 35.3% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Gazişehir Gaziantep expected goals | 1.39 |
| Kasimpasa SK expected goals | 1.41 |
| Expected total goals | 2.81 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 76.5% |
| Under 1.5 | 23.5% |
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 28.8% |
| Under 3.5 | 71.2% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.27% |
| 2 | 2-1 | 8.54% |
| 3 | 1-0 | 8.08% |
| 4 | 1-2 | 8.08% |
| 5 | 0-0 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Gazişehir Gaziantep win | 36.9% | 37.4% | 2.61 | -3.8% |
| Draw | 27.8% | 28.0% | 3.46 | -3.6% |
| Kasimpasa SK win | 35.3% | 34.7% | 2.79 | -1.5% |
| Over 2.5 | 51.0% | 51.0% | 1.93 | -1.6% |
| Under 2.5 | 49.0% | 49.0% | 1.96 | -3.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T17:00:00+00:00 |
| Fixture id | 51baab3ec98943f452377895491bfd6a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:29:41Z |
| Market best draw last update utc | 2026-11-05T12:29:41Z |
| Market best away last update utc | 2026-11-05T12:29:41Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Gaziantep |
| Matched away-team name | Kasimpasa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3919 |
| Dc lambda away | 1.4143 |
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
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.88 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.25 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.47 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.20 |
| Fair Under 4.5 odds | 1.16 |
| Score matrix json | [[0.07761140589956068,0.07664391668191159,0.06012420886799904,0.027365276298203213,0.009341391275365039,0.0025510165512985005,0.0005805421317130106,0.00011324197121866156,1.9328099420954876e-05,2.9323672384879033e-06,4.00396318886438e-07,4.9701455618771364e-08,5.655351193130121e-09,5.940020508972219e-10,5.793374802363322e-11],[0.08080505109906934,0.13265614551411986,0.08079324961046262,0.03677270171610974,0.012552703332471854,0.0034279855131562507,0.0007801164662283618,0.00015217143009959474,2.5972565633943707e-05,3.940434023320577e-06,5.380415034803098e-07,6.678744195415082e-08,7.599504578671986e-09,7.982035334989539e-10,7.78497688879248e-11],[0.06253294680783246,0.08538480918197887,0.05549439664241173,0.024707069951834665,0.008433987845503909,0.0023032160791798205,0.0005241494696387317,0.00010224188032652264,1.7450607815017834e-05,2.6475231492746132e-06,3.615026485164291e-07,4.4873559005929664e-08,5.106002073877543e-09,5.363019201094102e-10,5.230618355151972e-11],[0.028010015019712693,0.038245915309127416,0.02611119695586566,0.011313683972275569,0.0037777865635311688,0.0010316660299045763,0.00023477918867748638,4.5796604026837045e-05,7.816548107093882e-06,1.185889470459603e-06,1.6192575484612887e-07,2.0099949321221206e-08,2.287101473396109e-09,2.4022256433122073e-10,2.3429201112243253e-11],[0.009409770946212575,0.01284845089993191,0.00877187614191644,0.003992481877045095,0.0012974226621516125,0.00034658107207577384,7.887244568908597e-05,1.5385052585785914e-05,2.625915310150353e-06,3.983913709684489e-07,5.439783814190443e-08,6.75243904760721e-09,7.683359319963486e-10,8.070111011642677e-11,7.87087817567401e-12],[0.002528918008729993,0.003453078619113377,0.002357480928329105,0.001072997353081306,0.00036627761413180447,9.522234877422035e-05,2.119732238285684e-05,4.134801662213913e-06,7.057264789119994e-07,1.070694619798646e-07,1.4619662189376918e-08,1.8147481812209996e-09,2.064937166150669e-10,2.1688784122856736e-11,2.115333696936964e-12],[0.0005663816837692722,0.0007733585967317617,0.0005279862822881836,0.00024031069628206676,8.203228855297876e-05,2.2401986992174857e-05,4.853262790075948e-06,9.260386929953404e-07,1.5805595516616618e-07,2.3979497139521704e-08,3.2742496428801126e-09,4.0643473886816487e-10,4.62467579021869e-11,4.857464745004079e-12,4.737544898130995e-13],[0.0001087268639683399,0.00014845970015487693,0.00010135619554194931,4.6131838534950246e-05,1.5747531627708354e-05,4.300452966821133e-06,9.786663796513132e-07,1.8173356519997833e-07,3.034160324954722e-08,4.603283612857928e-09,6.285494494642508e-10,7.802225218661665e-11,8.877873525048869e-12,9.32475261287251e-13,9.094545506044783e-14],[1.8263019225838797e-05,2.4937005071536766e-05,1.7024956669213864e-05,7.748836150856115e-06,2.6451372032590543e-06,7.223537251634483e-07,1.643881029481226e-07,3.2065946304038896e-08,5.2101783676708805e-09,7.732206563788435e-10,1.0557842156928784e-10,1.3105518173892561e-11,1.4912301243209334e-12,1.5662930947283661e-13,1.527624851531876e-14],[2.726815590470854e-06,3.7232953307365377e-06,2.541962897734994e-06,1.1569635317617184e-06,3.9494024923198244e-07,1.0785321831253357e-07,2.4544465318892566e-08,4.787703567729153e-09,8.171635442167212e-10,1.1802254933722082e-10,1.576370710627754e-11,1.956759221235941e-12,2.2265264585742947e-13,2.3386015078544548e-14,2.280866712144922e-15],[3.664219401643905e-07,5.003261326732834e-07,3.4158194638058295e-07,1.5546956071729473e-07,5.307097879237306e-08,1.449301729282985e-08,3.298217390965272e-09,6.43358368769031e-10,1.0980817784300444e-10,1.665957403322234e-11,2.1655210526333004e-12,2.6294389425726706e-13,2.991944697797718e-14,3.1425480504584845e-15,3.064965628189772e-16],[4.476251569547726e-08,6.112040222427093e-08,4.1728034159998236e-08,1.899233612663778e-08,6.483210366994297e-09,1.7704832678798353e-09,4.029139403168485e-10,7.859338080825726e-11,1.3414290317834307e-11,2.0351522722889377e-12,2.778872535140082e-13,3.2837830642280194e-14,3.654993241809858e-15,3.8389719886677735e-16,3.744196430388202e-17],[5.012552586092915e-09,6.844325558388209e-09,4.672748220056056e-09,2.1267813501630997e-09,7.259965707098348e-10,1.982605388718575e-10,4.511871779610826e-11,8.800967686899232e-12,1.5021460384554596e-12,2.2789844643574193e-13,3.111810070551147e-14,3.862710090484357e-15,4.184170617889186e-16,4.298920351270425e-17,4.192789705489794e-18],[5.181330447785041e-10,7.074781122220994e-10,4.83008451513949e-10,2.1983922913755908e-10,7.504416307257999e-11,2.0493617752781083e-11,4.663791197534643e-12,9.097305427302704e-13,1.5527248587202513e-13,2.355720242809099e-14,3.216587953811025e-15,3.992771558810359e-16,4.5432322087737637e-17,4.5427632069941516e-18,4.3339652979375747e-19],[4.973234718875828e-11,6.790639481509569e-11,4.636095737932522e-11,2.1100991298194194e-11,7.203019398252783e-12,1.9670540674947755e-12,4.476481193181182e-13,8.73193394152658e-14,1.49036338331793e-14,2.261108380860957e-15,3.087401401902328e-16,3.8324114512526945e-17,4.360764167482797e-18,4.580268794112179e-19,4.2526676855129047e-20]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.18629075837174594, "-10": 4.725378563569732e-07, "-11": 5.7860691318665007e-08, "-12": 6.505860910180595e-09, "-13": 6.718518197851467e-10, "-14": 5.793374802363322e-11, "-2": 0.10644573447367282, "-3": 0.04247209029897501, "-4": 0.013342059200745807, "-5": 0.003441604872465159, "-6": 0.0007514063188789154, "-7": 0.00014203094963790043, "-8": 2.3650926540583717e-05, "-9": 3.517652218891352e-06, "0": 0.2784733173660487, "1": 0.1966832302815138, "10": 4.324421328572532e-07, "11": 5.211095069667762e-08, "12": 5.7663916556943396e-09, "13": 5.860394395935997e-10, "14": 4.973234718875828e-11, "2": 0.11071023764115878, "3": 0.043472752631077784, "4": 0.013439724054907442, "5": 0.0034117914822935267, "6": 0.0007330781916305369, "7": 0.00013636798772034535, "8": 2.2347635776919136e-05, "9": 3.271073549871439e-06} |
| Raw goal margin distribution | {"-1": 0.19072676969152358, "-10": 6.370937457974586e-07, "-11": 8.072501120019169e-08, "-12": 9.3933525936113e-09, "-13": 1.0030804236020759e-09, "-14": 8.884296376851214e-11, "-2": 0.11125785816500726, "-3": 0.04560487588670479, "-4": 0.014758360685902652, "-5": 0.003928088946138928, "-6": 0.0008857996864326926, "-7": 0.000173050174357123, "-8": 2.9796494403200946e-05, "-9": 4.583967205452102e-06, "0": 0.2754277911556094, "1": 0.18751840313102106, "10": 5.429291804356154e-07, "11": 6.77020688998398e-08, "12": 7.752975923029397e-09, "13": 8.147747273992435e-10, "14": 7.101969734595448e-11, "2": 0.10775530574174177, "3": 0.04346835756143301, "4": 0.01384375985150262, "5": 0.003626195664821226, "6": 0.0008047471134238728, "7": 0.00015472123765803257, "8": 2.6217848259693915e-05, "9": 3.969422800729087e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 35.7% |
| Unadjusted draw probability | 27.5% |
| Unadjusted away-win probability | 36.7% |
| Raw p over 1 5 | 78.1% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 58.0% |
| P home draw | 64.7% |
| P draw away | 63.1% |
| P home away | 72.2% |
| Raw p home draw | 63.3% |
| Raw p draw away | 64.3% |
| Raw p home away | 72.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9654 |
| Totals anchor target over 2 5 | 0.5096 |
| Totals anchor reference over odds | 1.89 |
| Totals anchor reference under odds | 1.96 |
| Totals anchor reference last update utc | 2026-11-05T12:31:26Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5309 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.88, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.84, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.29, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.84, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.79, "draw": 3.46, "home": 2.61}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.93, "under": 1.95}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.53, "home_away": 1.34, "home_draw": 1.48}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.76, "draw": 3.39, "home": 2.57}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.89, "under": 1.96}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.89, "under": 1.96}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.27, "under": 3.79}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.57 |
| Reference draw odds | 3.39 |
| Reference away odds | 2.76 |
| Market reference 1x2 last update utc | 2026-11-05T12:31:26Z |
| Market reference home last update utc | 2026-11-05T12:31:26Z |
| Market reference draw last update utc | 2026-11-05T12:31:26Z |
| Market reference away last update utc | 2026-11-05T12:31:26Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.96 |
| Market reference over 2 5 last update utc | 2026-11-05T12:31:26Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:31:26Z |
| Market best over 2 5 last update utc | 2026-11-05T12:29:41Z |
| Market best under 2 5 last update utc | 2026-11-05T12:31:26Z |
| Home probability edge | -0.5% |
| Draw probability edge | -0.1% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0163 |
| Raw ev home | -0.0677 |
| Raw edge prob draw | -0.0044 |
| Raw ev draw | -0.0470 |
| Raw edge prob away | 0.0207 |
| Raw ev away | 0.0250 |
| Market p home draw | 66.0% |
| Market home draw odds | 1.48 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T12:29:41Z |
| Market reference home draw last update utc | 2026-11-05T12:31:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 62.5% |
| Market draw away odds | 1.53 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T12:29:41Z |
| Market reference draw away last update utc | 2026-11-05T12:31:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.5% |
| Market home away odds | 1.34 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T12:29:41Z |
| Market reference home away last update utc | 2026-11-05T12:31:27Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.42 |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 76.2% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T12:31:26Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market reference over 1 5 last update utc | 2026-11-05T12:31:27Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.7% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T12:31:26Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 2.95 |
| Market reference under 3 5 last update utc | 2026-11-05T12:31:27Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,396.7846 |
| Elo away rating | 1,500.7901 |
| Elo rating diff | -44.0056 |
| Elo home expectancy | 0.4370 |

</details>


---

## 2026-11-07 — Eyüpspor vs Kocaelispor

The model's most likely 1X2 outcome is **Kocaelispor win** at **45.0%**. Expected goals are 0.80 for Eyüpspor and 0.87 for Kocaelispor (1.67 combined). The most likely exact score is 1-1 at 14.3%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 43.4%; Under 3.5 goals: 77.5%; Double Chance 1X: 55.0%; Double Chance X2: 75.1%; Double Chance 12 (either team wins): 69.9%; Under 4.5 goals: 90.2%; BTTS Yes (both teams score): 50.2%; BTTS No (at least one team does not score): 49.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eyüpspor win | 24.9% | 4.02 |
| Draw | 30.1% | 3.32 |
| Kocaelispor win | 45.0% | 2.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eyüpspor expected goals | 0.80 |
| Kocaelispor expected goals | 0.87 |
| Expected total goals | 1.67 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 43.4% |
| Under 2.5 | 56.6% |
| Over 3.5 | 22.5% |
| Under 3.5 | 77.5% |
| Over 4.5 | 9.8% |
| Under 4.5 | 90.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.32% |
| 2 | 0-1 | 12.03% |
| 3 | 0-0 | 10.25% |
| 4 | 1-2 | 9.83% |
| 5 | 0-2 | 8.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eyüpspor win | 24.9% | 22.8% | 4.09 | +1.7% |
| Draw | 30.1% | 27.2% | 3.50 | +5.5% |
| Kocaelispor win | 45.0% | 49.9% | 2.00 | -10.0% |
| Over 2.5 | 43.4% | 43.7% | 2.20 | -4.6% |
| Under 2.5 | 56.6% | 56.3% | 1.73 | -2.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T10:30:00+00:00 |
| Fixture id | a3dad1ddaa98a6ff741be7f63250f2ee |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:31:26Z |
| Market best draw last update utc | 2026-11-05T12:29:41Z |
| Market best away last update utc | 2026-11-05T12:29:41Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Eyupspor |
| Matched away-team name | Kocaelispor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7986 |
| Dc lambda away | 0.8690 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 50.2% |
| P btts no | 49.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.76 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.31 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.45 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.24 |
| Fair Under 4.5 odds | 1.11 |
| Score matrix json | [[0.10248438171866331,0.1202806744592396,0.08509510331005053,0.035659491423015,0.011207454475214417,0.002817920969740713,0.0005904313217946038,0.00010603840293187099,1.666345376866998e-05,2.327632118370913e-06,2.926214588114086e-07,3.34430066898929e-08,3.503611147497194e-09,3.3881636356696725e-10,3.042483075815171e-11],[0.06952684574952951,0.14315019648619934,0.09831201547572585,0.04119809878909801,0.012948188496771429,0.003255598491691364,0.0006821367033791299,0.00012250821380491915,1.9251609799632694e-05,2.6891583174804167e-06,3.380712199429092e-07,3.8637351191313826e-08,4.047789590179477e-09,3.9144108512399724e-10,3.51503942764292e-11],[0.045709136895780066,0.05746386730913009,0.04740347164570271,0.023798479396439667,0.00747964605694802,0.001880627890724403,0.0003940428504729773,7.076805211464045e-05,1.1120878211158965e-05,1.553418256991446e-06,1.9529010315567272e-07,2.2319238831060082e-08,2.3382447247420254e-09,2.261197208864548e-10,2.030496451418033e-11],[0.01760288273191095,0.02212970504936606,0.013910330854052494,0.007650001123606395,0.0028804598239703686,0.0007242419015319224,0.000151748437167802,2.725323222313536e-05,4.282721755898386e-06,5.982313661659718e-07,7.520747531046621e-08,8.595282485960382e-09,9.0047308882665e-10,8.708015947035247e-11,7.819572485774232e-12],[0.005084237553750694,0.006391718855312685,0.004017718437961383,0.001683643248619825,0.0006944410351646138,0.00020918266228594451,4.38294746787625e-05,7.871546316602156e-06,1.2369777788799644e-06,1.727870613021137e-07,2.172216199583468e-08,2.4825739434708666e-09,2.600834854199664e-10,2.5151347293995306e-11,2.2585257592142743e-12],[0.0011747835577457226,0.0014768952350417358,0.0009283495333704277,0.00038902910902128,0.0001222683177717789,4.0344954184741465e-05,1.0127407630522274e-05,1.81882988137646e-06,2.858208611540937e-07,3.992484545872164e-08,5.0192066129109334e-09,5.736331197833215e-10,6.009589423829627e-11,5.811567406865291e-12,5.218636813523305e-13],[0.00022620835358941384,0.00028438092901463056,0.00017875668936173414,7.490880653703186e-05,2.354315795189897e-05,5.919520675572913e-06,1.6277233192534518e-06,3.502215452477854e-07,5.503572636583523e-08,7.687657440370822e-09,9.664643812434345e-10,1.1045490272228543e-10,1.1571657777722279e-11,1.1190360013239496e-12,1.0048653079835886e-13],[3.733469678338497e-05,4.693582525696534e-05,2.9503007689254522e-05,1.2363370026296902e-05,3.885694977705816e-06,9.769909290203836e-07,2.0470625393583014e-07,4.8247894390216606e-08,9.083405292146393e-09,1.2688141483569415e-09,1.595107079518305e-10,1.8230097323725875e-11,1.9098513717867296e-12,1.8469198478387413e-13,1.65848612513246e-14],[5.391686984878719e-06,6.778233117327538e-06,4.260674286330929e-06,1.7854550057492382e-06,5.611523018402715e-07,1.410920599384115e-07,2.9562635836385787e-08,5.309296060071411e-09,1.0949448628662363e-09,1.8323568474702505e-10,2.3035724998720606e-11,2.6326979175346496e-12,2.7581101954731527e-13,2.6672276899642408e-14,2.3951012934054664e-15],[6.921244501465147e-07,8.701137292377046e-07,5.46937694259809e-07,2.2919673704747359e-07,7.20344540491505e-08,1.811182004422476e-08,3.794920426672434e-09,6.815480250518736e-10,1.0710217895187452e-10,1.9633652089682614e-11,2.9570686397746167e-12,3.3795630267222034e-13,3.540553277367773e-14,3.4238884851984482e-15,3.074563064199753e-16],[7.996247375834102e-08,1.0052591875090338e-07,6.318876759149232e-08,2.6479541457864052e-08,8.322279527016109e-09,2.092493531612034e-09,4.3843448236592397e-10,7.874055895110041e-11,1.2373721477528326e-11,1.72842148660816e-12,2.851641658278551e-13,3.904474401702287e-14,4.0904695459262786e-15,3.955684459510286e-16,3.552102057475268e-17],[8.39838086160247e-09,1.0558139492833366e-08,6.636654814012416e-09,2.781120490041584e-09,8.740809259581894e-10,2.1977256083931924e-10,4.604834733973535e-11,8.270044337614331e-12,1.2995999343108536e-12,1.8153442798408023e-13,2.282184917536494e-14,3.4229727335111848e-15,4.2961803874772633e-16,4.15461692189383e-17,3.730738249558873e-18],[8.085676271999496e-10,1.0165018636386823e-09,6.389546180318425e-10,2.6775684892683127e-10,8.415354720503763e-11,2.115895682392264e-11,4.433378714128067e-12,7.962118219091212e-13,1.251210742298289e-13,1.7477519072906232e-14,2.1972102408938607e-15,2.5111390355234507e-16,3.4525089023475396e-17,3.999924273283644e-18,3.5918282629234454e-19],[7.185798367523836e-11,9.03372480742849e-11,5.6784354168060537e-11,2.3795742782513792e-11,7.478785964031197e-12,1.880411635207006e-12,3.9399753904219084e-13,7.075991441669356e-14,1.1119599408859303e-14,1.553239627678036e-15,1.952676465269538e-16,2.2316672316671388e-17,2.337975847349935e-18,2.967166806871845e-19,3.1920834819372144e-20],[5.929922545764885e-12,7.454883322347561e-12,4.686004321380836e-12,1.9636914981776037e-12,6.171704135686837e-13,1.5517684717300348e-13,3.251378302376808e-14,5.8393067878487625e-15,9.176205601937935e-16,1.281776946145698e-16,1.611403438248215e-17,1.8416344510189573e-18,1.9293633051704407e-19,1.8657888433890966e-20,2.1987697332026856e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2454912987164747, "-10": 3.3368639341269405e-07, "-11": 3.772473557344461e-08, "-12": 3.915357197135371e-09, "-13": 3.7396675784339647e-10, "-14": 3.042483075815171e-11, "-2": 0.13454279469010694, "-3": 0.05064822146469304, "-4": 0.01488562693719998, "-5": 0.0035752863656500307, "-6": 0.0007246809527307084, "-7": 0.00012692118226926416, "-8": 1.955676346733139e-05, "-9": 2.6889487234446843e-06, "0": 0.30142451404960185, "1": 0.14271308512418296, "10": 9.118398078240232e-08, "11": 9.47363077090739e-09, "12": 9.035908795956154e-10, "13": 7.931286699758591e-11, "14": 5.929922545764885e-12, "2": 0.07227013989775105, "3": 0.025001890589147, "4": 0.0067528325591335635, "5": 0.0014905271232587445, "6": 0.0002776425964269017, "7": 4.468724277614981e-05, "8": 6.3278566686705815e-06, "9": 7.995624145231685e-07} |
| Raw goal margin distribution | {"-1": 0.21521587510072482, "-10": 1.3593522841877555e-08, "-11": 1.0666933876584465e-09, "-12": 7.301997980240789e-11, "-2": 0.08922542845312874, "-3": 0.024475433099726534, "-4": 0.005142562589077168, "-5": 0.0008738440252535079, "-6": 0.00012452290315270975, "-7": 1.527041347178743e-05, "-8": 1.6429502914193431e-06, "-9": 1.5742163730122032e-07, "0": 0.3694926947917807, "1": 0.19675705304731692, "10": 5.840284725133592e-09, "11": 4.2116454318888335e-10, "12": 2.6495011192166013e-11, "2": 0.07535447386502359, "3": 0.018995948575168023, "4": 0.0036679244837574424, "5": 0.000572776143044057, "6": 7.500849242243204e-05, "7": 8.45322046482369e-06, "8": 8.358070363210647e-07, "9": 7.359634120173803e-08} |
| Research history json | {"away": [{"away": "Rizespor", "away_goals": 0.0, "away_xg": 1.17, "date": "2026-10-31T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 0.0, "home_xg": 0.62, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 1.54, "date": "2026-10-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.5, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 0.83, "date": "2026-10-18T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.61, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 1.0, "away_xg": 1.65, "date": "2026-10-11T00:00:00+00:00", "home": "Besiktas", "home_goals": 2.0, "home_xg": 2.21, "source": "pipeline training history"}, {"away": "Gaziantep", "away_goals": 0.0, "away_xg": 0.88, "date": "2026-09-19T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 2.0, "home_xg": 1.16, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-09-13T00:00:00+00:00", "home": "Galatasaray", "home_goals": 1.0, "home_xg": 2.26, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 1.74, "date": "2026-09-06T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 0.77, "date": "2026-08-29T00:00:00+00:00", "home": "Konyaspor", "home_goals": 1.0, "home_xg": 0.86, "source": "pipeline training history"}, {"away": "Amedspor", "away_goals": 0.0, "away_xg": 0.59, "date": "2026-08-24T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 2.0, "home_xg": 1.3, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.44, "date": "2026-08-16T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 2.0, "home_xg": 1.96, "source": "pipeline training history"}], "h2h": [{"away": "Kocaelispor", "away_goals": 1.0, "away_xg": null, "date": "2026-03-09T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": null, "date": "2025-10-04T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Eyupspor", "away_goals": 1.0, "away_xg": 0.98, "date": "2026-11-01T00:00:00+00:00", "home": "Amedspor", "home_goals": 5.0, "home_xg": 4.95, "source": "pipeline training history"}, {"away": "Kasimpasa", "away_goals": 1.0, "away_xg": 0.59, "date": "2026-10-24T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 0.43, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.43, "date": "2026-10-17T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 2.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 4.0, "away_xg": 3.21, "date": "2026-10-12T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 1.39, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-20T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 8.0, "home_xg": 5.14, "source": "pipeline training history"}, {"away": "Rizespor", "away_goals": 2.0, "away_xg": 2.05, "date": "2026-09-12T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 1.43, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-06T00:00:00+00:00", "home": "Corum", "home_goals": 3.0, "home_xg": 2.58, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 0.66, "date": "2026-08-30T00:00:00+00:00", "home": "Eyupspor", "home_goals": 2.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Gaziantep", "away_goals": 1.0, "away_xg": 1.16, "date": "2026-08-23T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 0.49, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.09, "date": "2026-08-16T00:00:00+00:00", "home": "Besiktas", "home_goals": 1.0, "home_xg": 1.29, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 29.5% |
| Unadjusted draw probability | 36.9% |
| Unadjusted away-win probability | 33.5% |
| Raw p over 1 5 | 50.9% |
| Raw p under 3 5 | 91.2% |
| Raw p btts yes | 33.2% |
| P home draw | 55.0% |
| P draw away | 75.1% |
| P home away | 69.9% |
| Raw p home draw | 66.5% |
| Raw p draw away | 70.5% |
| Raw p home away | 63.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.4468 |
| Totals anchor target over 2 5 | 0.4338 |
| Totals anchor reference over odds | 2.18 |
| Totals anchor reference under odds | 1.70 |
| Totals anchor reference last update utc | 2026-11-05T12:31:26Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.2529 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.17, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.4, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.88, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.51, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.03, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.0, "draw": 3.5, "home": 4.07}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.2, "under": 1.73}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.26, "home_away": 1.33, "home_draw": 1.86}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.94, "draw": 3.46, "home": 4.09}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.18, "under": 1.7}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.37, "under": 3.07}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.09 |
| Reference draw odds | 3.46 |
| Reference away odds | 1.94 |
| Market reference 1x2 last update utc | 2026-11-05T12:31:26Z |
| Market reference home last update utc | 2026-11-05T12:31:26Z |
| Market reference draw last update utc | 2026-11-05T12:31:26Z |
| Market reference away last update utc | 2026-11-05T12:31:26Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.20 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-11-05T12:29:41Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:29:41Z |
| Market best over 2 5 last update utc | 2026-11-05T12:29:41Z |
| Market best under 2 5 last update utc | 2026-11-05T12:29:41Z |
| Home probability edge | +2.0% |
| Draw probability edge | +2.9% |
| Away probability edge | -4.9% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.0670 |
| Raw ev home | 0.2083 |
| Raw edge prob draw | 0.0972 |
| Raw ev draw | 0.2932 |
| Raw edge prob away | -0.1642 |
| Raw ev away | -0.3299 |
| Market p home draw | 53.0% |
| Market home draw odds | 1.86 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T12:29:41Z |
| Market reference home draw last update utc | 2026-11-05T12:31:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 75.5% |
| Market draw away odds | 1.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T12:29:41Z |
| Market reference draw away last update utc | 2026-11-05T12:31:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.5% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T12:29:41Z |
| Market reference home away last update utc | 2026-11-05T12:31:27Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.78 |
| Market reference dc draw away odds | 1.25 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 70.5% |
| Market over 1 5 odds | 1.37 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T12:31:26Z |
| Market reference over 1 5 odds | 1.35 |
| Market reference over 1 5 opposite odds | 2.85 |
| Market reference over 1 5 last update utc | 2026-11-05T12:31:27Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 78.2% |
| Market under 3 5 odds | 1.25 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T12:31:26Z |
| Market reference under 3 5 odds | 1.23 |
| Market reference under 3 5 opposite odds | 3.60 |
| Market reference under 3 5 last update utc | 2026-11-05T12:31:27Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,370.1212 |
| Elo away rating | 1,438.4311 |
| Elo rating diff | -8.3099 |
| Elo home expectancy | 0.4880 |

</details>


---

## 2026-11-07 — Galatasaray vs Amed SK

The model's most likely 1X2 outcome is **Galatasaray win** at **64.6%**. Expected goals are 2.21 for Galatasaray and 1.53 for Amed SK (3.74 combined). The most likely exact score is 2-1 at 10.9%. Goal-market probabilities: at least one goal: 97.3%; Over 2.5 goals: 73.5%; Under 3.5 goals: 47.6%; Double Chance 1X: 83.3%; Double Chance X2: 35.4%; Double Chance 12 (either team wins): 81.3%; Under 4.5 goals: 66.8%; BTTS Yes (both teams score): 69.4%; BTTS No (at least one team does not score): 30.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 64.6% | 1.55 |
| Draw | 18.7% | 5.35 |
| Amed SK win | 16.7% | 5.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 2.21 |
| Amed SK expected goals | 1.53 |
| Expected total goals | 3.74 |
| Over 0.5 | 97.3% |
| Under 0.5 | 2.7% |
| Over 1.5 | 89.9% |
| Under 1.5 | 10.1% |
| Over 2.5 | 73.5% |
| Under 2.5 | 26.5% |
| Over 3.5 | 52.4% |
| Under 3.5 | 47.6% |
| Over 4.5 | 33.2% |
| Under 4.5 | 66.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.92% |
| 2 | 3-1 | 8.06% |
| 3 | 1-1 | 7.51% |
| 4 | 2-0 | 7.15% |
| 5 | 3-2 | 6.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 64.6% | 69.8% | 1.45 | -6.3% |
| Draw | 18.7% | 17.3% | 5.15 | -3.7% |
| Amed SK win | 16.7% | 12.9% | 6.79 | +13.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T16:00:00+00:00 |
| Fixture id | e300554369b00b495db88afb743c95ab |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:29:41Z |
| Market best draw last update utc | 2026-11-05T12:29:41Z |
| Market best away last update utc | 2026-11-05T12:31:26Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Galatasaray |
| Matched away-team name | Amedspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2146 |
| Dc lambda away | 1.5271 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 69.4% |
| P btts no | 30.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 37.22 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.95 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.77 |
| Fair Over 3.5 odds | 1.91 |
| Fair Under 3.5 odds | 2.10 |
| Fair Over 4.5 odds | 3.01 |
| Fair Under 4.5 odds | 1.50 |
| Score matrix json | [[0.02686823414423417,0.018580876033283403,0.018044369368517565,0.009185142355466398,0.003506641256082617,0.001070993343204319,0.0002725843757181058,5.946594935074042e-05,1.1351253102861534e-05,1.926046357054053e-06,2.9412515801690727e-07,4.083240178496581e-08,5.196238996371827e-09,6.103953314694843e-10,6.65807381099314e-11,6.7783311811244284e-12,6.469463087029953e-13,5.811453345677038e-14],[0.05507650954982225,0.0751175499203623,0.039961643770579654,0.02034171321230089,0.0077659210939941,0.002371856482635795,0.0006036741710063817,0.00013169521394190188,2.5138852102954174e-05,4.265484530620649e-06,6.513790838899642e-07,9.042875708778732e-08,1.1507758873640527e-08,1.3518012349030284e-09,1.4745185514620863e-10,1.5011511374385068e-11,1.4327482107624642e-12,1.2870232461239427e-13],[0.07153003319937343,0.10923300075653349,0.05792057018113964,0.022524707859603206,0.00859932996190153,0.002626395023796241,0.0006684581678245402,0.00014582823922399348,2.7836657297989958e-05,4.7232399714389225e-06,7.212825890006645e-07,1.0013322448562022e-07,1.2742727421344353e-08,1.4968713589978602e-09,1.6327582273239606e-10,1.6622489202859414e-11,1.586505253858278e-12,1.4251416448998748e-13],[0.052804241353322366,0.08063697831117692,0.06157007566540956,0.021764935895059657,0.006348118048812571,0.0019388331099910127,0.0004934630231475397,0.00010765197771753916,2.0549320399947197e-05,3.486746647053214e-06,5.324585801237115e-07,7.391942540397726e-08,9.40681870482007e-09,1.1050065682912478e-09,1.2053197188784814e-10,1.2270900662303513e-11,1.1711752754195607e-12,1.0520549203467029e-13],[0.02923549501013316,0.044645314782091834,0.03408877002597722,0.017352238751975866,0.004600494152283895,0.001073450621766329,0.0002732097911299206,5.960238754938689e-05,1.1377297327205784e-05,1.930465462413258e-06,2.9479999642736873e-07,4.092608732108819e-08,5.208161205571245e-09,6.117958176367311e-10,6.673350042301063e-11,6.793883329980694e-12,6.484306571401117e-13,5.824787097759688e-14],[0.012949174484200687,0.019774591496227185,0.01509881843509647,0.007685765786177494,0.0029342194543515855,0.0006223454914012191,0.00012101184723936212,2.6399474877523076e-05,5.03930609683721e-06,8.550542448434016e-07,1.3057472057020424e-07,1.812724722097978e-08,2.306832436714739e-09,2.709805593692313e-10,2.955803350069937e-11,3.0091907332073495e-12,2.8720709935993577e-13,2.5799523639352804e-14],[0.004779610075701783,0.007298908271996176,0.0055730552408286204,0.002836857564620693,0.0010830362109530804,0.00033077936625766126,5.8465022368415825e-05,9.744188424659568e-06,1.8600350334591458e-06,3.1560512903053746e-07,4.819583293365565e-08,6.690864623674902e-09,8.514642822158285e-10,1.0002038457823982e-10,1.0910029431624732e-11,1.1107085139438589e-12,1.060096879217059e-13,9.522743189954675e-15],[0.0015121541423546467,0.002309199747124782,0.0017631811872755967,0.0008975137824357851,0.0003426467152704539,0.00010465066835363663,2.6635214198727753e-05,4.035219034023924e-06,5.884705313240502e-07,9.98499031622003e-08,1.5248007109483532e-08,2.116829301214203e-09,2.6938290384088346e-10,3.164405390071133e-11,3.4516719851504055e-12,3.514015691043945e-13,3.3538926017305695e-14,3.0127678478364494e-15],[0.0004186081813727253,0.000639253551932904,0.00048809975753314253,0.0002484578798543443,9.485456165821414e-05,2.897034418114355e-05,7.373400808756614e-06,1.6085525000511068e-06,2.1323289968229935e-07,2.7641352956177992e-08,4.22109118830975e-09,5.859998258365062e-10,7.457301098560156e-11,8.759993100974863e-12,9.555230461817053e-13,9.727815945089893e-14,9.28454873220589e-15,8.340216346709267e-16],[0.00010300702354431625,0.0001573012869906388,0.00012010683367754008,6.113809480741997e-05,2.334088653970602e-05,7.1287400914339425e-06,1.8143746455662544e-06,3.9581693005063874e-07,7.555614943439047e-08,8.90299782345368e-09,1.03868500130862e-09,1.441971288257271e-10,1.8350200115952413e-11,2.1555737698225457e-12,2.351258033046859e-13,2.3937261875884056e-14,2.2846513097772836e-15,2.0522791952440033e-16],[2.2812268451606476e-05,3.483645156555586e-05,2.6599247686695028e-05,1.353984013300411e-05,5.169148193212131e-06,1.5787538275732854e-06,4.018172748059137e-07,8.765889698891454e-08,1.6732909123672236e-08,2.8391895034426643e-09,3.0109485915934506e-10,3.193436233314865e-11,4.063894643123148e-12,4.773803359464862e-13,5.2071720551933934e-14,5.30122340321912e-15,5.059662652472548e-16,4.5450438551319926e-17],[4.592798838564558e-06,7.013630171388247e-06,5.3552321699747885e-06,2.7259788814571773e-06,1.0407057004662287e-06,3.17850842455228e-07,8.089795703389665e-08,1.7648384295257815e-08,3.3688401375793998e-09,5.716146240142055e-10,8.729085932807322e-11,8.415599196824301e-12,8.181847691552275e-13,9.611108413614078e-14,1.0483610526516434e-14,1.0672964304679419e-15,1.0186629533621824e-16,9.150546419071792e-18],[8.476133992656468e-07,1.294384343778598e-06,9.88322524673812e-07,5.030867467211857e-07,1.920650408200796e-07,5.8660229307393015e-08,1.4929935920419807e-08,3.257056868775304e-09,6.217285234919367e-10,1.0549301886735025e-10,1.610976326213585e-11,2.2364639958558056e-12,1.9764672600831938e-13,1.7737559513318922e-14,1.9347785669043096e-15,1.9697243168084529e-16,1.8799699245594675e-17,1.6887579944240809e-18],[1.44396310539019e-07,2.2050657035746302e-07,1.683670011695755e-07,8.570401337514739e-08,3.271949606031859e-08,9.993141560408179e-09,2.54340913600511e-09,5.548602646848044e-10,1.0591539141180017e-10,1.7971403856128108e-11,2.744400195566525e-12,3.8099580532199665e-13,4.848466351536478e-14,3.955214064502887e-15,3.296017819125994e-16,3.355550117217901e-17,3.2026478258353686e-18,2.8769061933114444e-19],[2.2841766970943212e-08,3.4881498542900956e-08,2.663364314473083e-08,1.355734848544293e-08,5.175832413076342e-09,1.5807953124176975e-09,4.0233686428364765e-10,8.777224861255293e-11,1.6754546430123877e-11,2.8428608562783384e-12,4.3413124274530665e-13,6.026897342172921e-14,7.669693093600829e-15,9.009487172176817e-16,6.824659612780351e-17,5.30807840939266e-18,5.066205296704003e-19,4.5509210463605346e-20],[3.3724077065872135e-09,5.149979625176622e-09,3.932248477538646e-09,2.001636150625184e-09,7.641710529691906e-10,2.3339202702295356e-10,5.940188180189104e-11,1.2958883961210443e-11,2.473677346117758e-12,4.1972610405596415e-13,6.40960723645847e-14,8.898241134063482e-15,1.1323700188746873e-15,1.3301801043018479e-16,1.450934641822211e-17,1.0258067454324489e-18,7.47985469227998e-20,6.719077919120573e-21],[4.66790195972873e-10,7.128319609153192e-10,5.442802878960943e-10,2.770555082031431e-10,1.0577236995264243e-10,3.230484553209615e-11,8.22208299230889e-12,1.7936977109937427e-12,3.423928639803988e-13,5.809618747594544e-14,8.871827128646195e-15,1.2316457807489467e-15,1.5673645330363364e-16,1.8411624144775355e-17,2.0083042286883258e-18,2.0445779907134391e-19,1.3551665039611188e-20,9.30017949044853e-22],[6.080992112571214e-11,9.28623944828232e-11,7.090474834900951e-11,3.6092710915154504e-11,1.3779230004379999e-11,4.208432665752138e-12,1.07111122419636e-12,2.3366946707517963e-13,4.460437094069713e-14,7.568335000596574e-15,1.1557550106842441e-15,1.6044956262644405e-16,2.0418448041851583e-17,2.3985281218397985e-18,2.6162679250030435e-19,2.6635226580010813e-20,2.542153969311873e-21,1.5858492059984635e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.08862016955304908, "-10": 3.984715008079422e-07, "-11": 5.396465460266458e-08, "-12": 6.7242611848503336e-09, "-13": 7.756990989649495e-10, "-14": 8.328396023020941e-11, "-15": 8.35359355637688e-12, "-16": 7.756486333153896e-13, "-17": 5.811453345677038e-14, "-2": 0.04922581917310536, "-3": 0.020135894648024736, "-4": 0.006666890625276518, "-5": 0.0018431130832656762, "-6": 0.00043591680493701077, "-7": 8.990383649667986e-05, "-8": 1.6417430060572544e-05, "-9": 2.687607983067057e-06, "0": 0.18695685247149296, "1": 0.24652514579596485, "10": 3.090534284123624e-05, "11": 6.0699050790079e-06, "12": 1.0968652297210844e-06, "13": 1.8350089229766615e-07, "14": 2.857211959493108e-08, "15": 4.156144415851542e-09, "16": 5.596525904556963e-10, "17": 6.080992112571214e-11, "2": 0.1951370207407729, "3": 0.11575875470526449, "4": 0.05558305893717661, "5": 0.022284725727531585, "6": 0.007643550176182285, "7": 0.0022861563677421828, "8": 0.0006054371687596063, "9": 0.00014373615555812473} |
| Raw goal margin distribution | {"-1": 0.13579418058821704, "-10": 6.105846018222818e-07, "-11": 8.269095048512982e-08, "-12": 1.0303698833608109e-08, "-13": 1.1886168132854737e-09, "-14": 1.2761741703544086e-10, "-15": 1.2800352308919489e-11, "-16": 1.1885394839194346e-12, "-17": 8.904987985048532e-14, "-2": 0.07542955302510583, "-3": 0.030854571007138246, "-4": 0.010215788957487298, "-5": 0.002824233265810463, "-6": 0.0006679626729400491, "-7": 0.00013776116509792475, "-8": 2.5156704999365524e-05, "-9": 4.1182670451163084e-06, "0": 0.21886288791639943, "1": 0.20041742777324678, "10": 2.5125101525413142e-05, "11": 4.934647777348324e-06, "12": 8.917179918698962e-07, "13": 1.4918063108593364e-07, "14": 2.32282621586402e-08, "15": 3.378818702610188e-09, "16": 4.5498049403283576e-10, "17": 4.943661197627301e-11, "2": 0.1586404487620449, "3": 0.09410833846322819, "4": 0.04518733236721221, "5": 0.018116802626863226, "6": 0.006213973265972913, "7": 0.0018585754294190003, "8": 0.0004922019603693649, "9": 0.00011685311241562661} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Galatasaray", "away_goals": 4.0, "away_xg": 2.8, "date": "2026-10-30T00:00:00+00:00", "home": "Konyaspor", "home_goals": 0.0, "home_xg": 1.38, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 0.31, "date": "2026-10-26T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 1.0, "away_xg": 1.92, "date": "2026-10-17T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 0.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Kasimpasa", "away_goals": 1.0, "away_xg": 0.51, "date": "2026-10-09T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.4, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-09-13T00:00:00+00:00", "home": "Galatasaray", "home_goals": 1.0, "home_xg": 2.26, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 3.0, "away_xg": 2.12, "date": "2026-09-04T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 2.0, "home_xg": 1.98, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 0.63, "date": "2026-08-29T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.92, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 4.0, "away_xg": 3.08, "date": "2026-08-21T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 0.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Corum", "away_goals": 2.0, "away_xg": 0.61, "date": "2026-08-14T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.9, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 52.5% |
| Unadjusted draw probability | 21.9% |
| Unadjusted away-win probability | 25.6% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.5% |
| Raw p btts yes | 70.5% |
| P home draw | 83.3% |
| P draw away | 35.4% |
| P home away | 81.3% |
| Raw p home draw | 74.4% |
| Raw p draw away | 47.5% |
| Raw p home away | 78.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7348 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -1.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.73, "draw": 5.15, "home": 1.45}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.79, "draw": 5.15, "home": 1.4}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.40 |
| Reference draw odds | 5.15 |
| Reference away odds | 6.79 |
| Market reference 1x2 last update utc | 2026-11-05T12:31:26Z |
| Market reference home last update utc | 2026-11-05T12:31:26Z |
| Market reference draw last update utc | 2026-11-05T12:31:26Z |
| Market reference away last update utc | 2026-11-05T12:31:26Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.79 |
| Market reference over 2 5 last update utc | 2026-11-05T12:31:27Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:31:27Z |
| Home probability edge | -5.2% |
| Draw probability edge | +1.4% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | +4.7% |
| Under 2.5 probability edge | -4.7% |
| Raw edge prob home | -0.1726 |
| Raw ev home | -0.2385 |
| Raw edge prob draw | 0.0456 |
| Raw ev draw | 0.1271 |
| Raw edge prob away | 0.1270 |
| Raw ev away | 0.7379 |
| Elo home rating | 1,693.8730 |
| Elo away rating | 1,457.7667 |
| Elo rating diff | 296.1063 |
| Elo home expectancy | 0.8461 |

</details>


---

## 2026-11-07 — Goztepe vs Basaksehir

The model's most likely 1X2 outcome is **Goztepe win** at **44.9%**. Expected goals are 1.52 for Goztepe and 1.35 for Basaksehir (2.87 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 55.2%; Under 3.5 goals: 67.6%; Double Chance 1X: 70.7%; Double Chance X2: 55.1%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 83.5%; BTTS Yes (both teams score): 58.6%; BTTS No (at least one team does not score): 41.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Goztepe win | 44.9% | 2.23 |
| Draw | 25.8% | 3.88 |
| Basaksehir win | 29.3% | 3.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Goztepe expected goals | 1.52 |
| Basaksehir expected goals | 1.35 |
| Expected total goals | 2.87 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 79.3% |
| Under 1.5 | 20.7% |
| Over 2.5 | 55.2% |
| Under 2.5 | 44.8% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.5% |
| Under 4.5 | 83.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.15% |
| 2 | 2-1 | 9.87% |
| 3 | 1-0 | 8.39% |
| 4 | 2-0 | 7.31% |
| 5 | 1-2 | 7.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Goztepe win | 44.9% | 46.9% | 2.09 | -6.1% |
| Draw | 25.8% | 25.2% | 3.77 | -2.8% |
| Basaksehir win | 29.3% | 27.9% | 3.48 | +2.0% |
| Over 2.5 | 55.2% | 58.4% | 1.67 | -7.9% |
| Under 2.5 | 44.8% | 41.6% | 2.31 | +3.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T16:00:00+00:00 |
| Fixture id | c7ad58db2278db2259846b11c28ae1c2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:29:41Z |
| Market best draw last update utc | 2026-11-05T12:29:41Z |
| Market best away last update utc | 2026-11-05T12:29:41Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Goztep |
| Matched away-team name | Buyuksehyr |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5169 |
| Dc lambda away | 1.3497 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.6% |
| P btts no | 41.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.43 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.82 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.08 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.06 |
| Fair Under 4.5 odds | 1.20 |
| Score matrix json | [[0.06481920913355618,0.058749332881785896,0.046446650409317655,0.020896084855998025,0.007050772635826198,0.0019032615958331834,0.00042813330411566156,8.254917760766439e-05,1.3926902733145465e-05,2.088544876960296e-06,2.8188735198287074e-07,3.458714250136557e-08,3.890139860817837e-09,4.038812035726777e-10,3.893654252731423e-11,3.503465974315833e-12],[0.08385113166559774,0.12150536717583198,0.0704550422051122,0.031697324295221985,0.01069533495436152,0.002887062358212498,0.0006494364985431079,0.00012521905758738094,2.112575419762484e-05,3.1681190388702192e-06,4.275956415805667e-07,5.2465324479008875e-08,5.90096305465177e-09,6.126484255117798e-10,5.906294044689047e-11,5.314416452194335e-12],[0.07312255348423409,0.09869226751735471,0.05671647896849732,0.024040875943994712,0.0081118904050849,0.002189696119139806,0.0004925659386754815,9.497255355828046e-05,1.6022855152003534e-05,2.4028639162065675e-06,3.243104584376792e-07,3.9792392108989777e-08,4.475592937299244e-09,4.646639778750205e-10,4.4796362334762724e-11,4.030725920332252e-12],[0.03697326248843825,0.049902183917648286,0.03367606470391278,0.0129019754270371,0.004101649066307753,0.0011071852051819603,0.00024905817529251317,4.802136939411809e-05,8.101703251883596e-06,1.2149701297980136e-06,1.6398245324060497e-07,2.0120393618444325e-08,2.26301277208329e-09,2.3494999017778e-10,2.26505720083678e-11,2.0380728020326623e-12],[0.014021208989922276,0.018924187444418296,0.012770827062376745,0.005745522736837997,0.0016509186974024738,0.00041987301383697776,9.444924497850367e-05,1.8210934360140315e-05,3.0723735700768865e-06,4.607478204483036e-07,6.218635015737827e-08,7.630169070741985e-09,8.581924582437207e-10,8.909905950260626e-11,8.589677580384479e-12,7.728894549923043e-13],[0.0042537615197047575,0.005741229618687303,0.003874420014122012,0.0017430796121872597,0.0005881512310258793,0.0001351995156820537,2.8654060013191045e-05,5.524842534956286e-06,9.32098257428758e-07,1.397819082733532e-07,1.8866126561587465e-08,2.314844576191114e-09,2.603588647742e-10,2.7030918020441833e-11,2.6059407562052688e-12,2.344795962313141e-13],[0.0010754236123959474,0.001451480969848034,0.0009795195965324,0.0004406803165971226,0.00014869468318216286,4.0138137282600206e-05,7.688862482304532e-06,1.3967746168510781e-06,2.3565036978884902e-07,3.533925539703555e-08,4.7696792320858034e-09,5.852322714216003e-10,6.582317075786889e-11,6.8338780557542674e-12,6.588263607976336e-13,5.928044937265903e-14],[0.0002330446877746698,0.00031453645384956456,0.0002122622526712934,9.549558481519358e-05,3.222219190327978e-05,8.697948941292605e-06,1.9565789733884344e-06,3.2125912476918057e-07,5.1065520803544107e-08,7.658029492065203e-09,1.0335912236019557e-09,1.26820045977281e-10,1.4263905033134587e-11,1.4809038591269658e-12,1.4276791190007637e-13,1.2846094930364113e-14],[4.4188259993307534e-05,5.964014341110518e-05,4.024764390627629e-05,1.8107186953374464e-05,6.109740612294433e-06,1.6492426104901214e-06,3.709924529887706e-07,7.153174396495823e-08,1.0276966864336847e-08,1.4520605531201261e-09,1.9598214467555164e-10,2.40467063099321e-11,2.7046192305118382e-12,2.807983540713324e-13,2.7070626110310784e-14,2.435784261388078e-15],[7.4476982262031075e-06,1.0052031701647898e-05,6.783528162797691e-06,3.0518708854931046e-06,1.0297645647879775e-06,2.779711458787055e-07,6.252882178383303e-08,1.2056298273019137e-08,2.03402260611422e-09,2.597582775071549e-10,3.303175711124743e-11,4.052945555168556e-12,4.558493103980239e-13,4.732708198635903e-14,4.5626112930109535e-15,4.1053859386409297e-16],[1.1297432392515718e-06,1.5247952469025686e-06,1.028995113313058e-06,4.6293907127226244e-07,1.5620524889112608e-07,4.216551385750466e-08,9.48501288896413e-09,1.8288229531673188e-09,3.085414067473436e-10,4.627034357457207e-11,5.318128834664548e-12,6.147923426726549e-13,6.914789790055792e-14,7.179057110488226e-15,6.921036681476608e-16,6.227470377868093e-17],[1.55791854057696e-07,2.1026961730763284e-07,1.4189866418280249e-07,6.38394050289098e-08,2.154073996000551e-08,5.814634115896955e-09,1.3079854717358596e-09,2.521951083380304e-10,4.254793137118702e-11,6.380691083528568e-12,8.611910297921622e-13,8.99835125850375e-14,9.535511117780027e-15,9.899936364036004e-16,9.54412559550145e-17,8.587696058266993e-18],[1.9693421657100633e-08,2.6579876466344938e-08,1.7937203734004906e-08,8.06984632911008e-09,2.7229336052528336e-09,7.350194406423433e-10,1.6534054089064552e-10,3.1879616802812307e-11,5.3784221145468374e-12,8.065738785360004e-13,1.0886190539030922e-13,1.3357187572337762e-14,1.2793515761700912e-15,1.2514365553620143e-16,1.2064590336727675e-17,1.0855581670903063e-18],[2.297923186787012e-09,3.1014678656375622e-09,2.092999230107421e-09,9.416284948524393e-10,3.177249934795353e-10,8.576560461661927e-11,1.9292729787844146e-11,3.71986706589679e-12,6.275801686747e-13,9.411492068857067e-14,1.2702530870962665e-14,1.5585809092586684e-15,1.7529918006893664e-16,1.549860686958285e-17,1.407754444939592e-18,1.2666814970995147e-19],[2.4898039499145016e-10,3.3604460700857346e-10,2.267768470353347e-10,1.0202561858099885e-10,3.4425560797704284e-11,9.292718850182195e-12,2.090370779432836e-12,4.030482727656614e-13,6.799842535376732e-14,1.0197368764268118e-14,1.3763215288607967e-15,1.6887252482792617e-16,1.8993698025332048e-17,1.9719593364836914e-18,1.6189224639934627e-19,1.3724517046070885e-20],[2.5178599651826307e-11,3.398312797003445e-11,2.293322509188814e-11,1.0317528030948437e-11,3.4813480521017217e-12,9.397432581539275e-13,2.1139258366516311e-13,4.075899671006289e-14,6.8764656309421306e-15,1.0312276419449111e-15,1.3918304197631905e-16,1.7077544177650855e-17,1.9207725913678535e-18,1.9941800905532699e-19,1.922507836861449e-20,1.473102578199449e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.15779687649690513, "-10": 3.390720435465332e-07, "-11": 4.097619299535572e-08, "-12": 4.549622721466413e-09, "-13": 4.669748699399004e-10, "-14": 4.4250958979508565e-11, "-15": 3.503465974315833e-12, "-2": 0.0874632679108245, "-3": 0.034049353534765896, "-4": 0.010481639356838572, "-5": 0.0026562525649150657, "-6": 0.0005706547555111334, "-7": 0.00010624967568175366, "-8": 1.7440338519120524e-05, "-9": 2.558287687702644e-06, "0": 0.2577371695817487, "1": 0.22259530618389675, "10": 1.3589270540921177e-06, "11": 1.8457023672078147e-07, "12": 2.3031983897804478e-08, "13": 2.6569010188874733e-09, "14": 2.8296352296148463e-10, "15": 2.5178599651826307e-11, "2": 0.13769642007235366, "3": 0.06024648609910156, "4": 0.02084385124439728, "5": 0.00593668519975911, "6": 0.0014334217700497259, "7": 0.00029995359388190003, "8": 5.533593704363704e-05, "9": 9.1227892127225e-06} |
| Raw goal margin distribution | {"-1": 0.1760496958622251, "-10": 3.782934837935217e-07, "-11": 4.571602730403665e-08, "-12": 5.075890690508946e-09, "-13": 5.209911986428577e-10, "-14": 4.936959490517592e-11, "-15": 3.908721978118835e-12, "-2": 0.09758039611841722, "-3": 0.037987940364703474, "-4": 0.01169408078204356, "-5": 0.002963508952572481, "-6": 0.0006366640353114839, "-7": 0.00011853988180557968, "-8": 1.9457712726561082e-05, "-9": 2.8542121957462127e-06, "0": 0.27092210036332093, "1": 0.19925431384177109, "10": 1.216432108862378e-06, "11": 1.6521649312330868e-07, "12": 2.0616886432368767e-08, "13": 2.378302573130468e-09, "14": 2.532924147257679e-10, "15": 2.2538411447798303e-11, "2": 0.1232577908777573, "3": 0.05392913469225129, "4": 0.018658197914070765, "5": 0.005314173763373699, "6": 0.0012831154265272528, "7": 0.0002685009336357472, "8": 4.9533498057287404e-05, "9": 8.16618794020031e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 40.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 58.9% |
| P home draw | 70.7% |
| P draw away | 55.1% |
| P home away | 74.2% |
| Raw p home draw | 67.3% |
| Raw p draw away | 59.8% |
| Raw p home away | 72.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5515 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.57, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.55, "price": 1.57, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.48, "draw": 3.77, "home": 2.09}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.67, "under": 2.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.39, "draw": 3.73, "home": 2.06}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.06 |
| Reference draw odds | 3.73 |
| Reference away odds | 3.39 |
| Market reference 1x2 last update utc | 2026-11-05T12:31:26Z |
| Market reference home last update utc | 2026-11-05T12:31:26Z |
| Market reference draw last update utc | 2026-11-05T12:31:26Z |
| Market reference away last update utc | 2026-11-05T12:31:26Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-11-05T12:29:41Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:29:41Z |
| Market best over 2 5 last update utc | 2026-11-05T12:29:41Z |
| Market best under 2 5 last update utc | 2026-11-05T12:29:41Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.6% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | -0.0673 |
| Raw ev home | -0.1598 |
| Raw edge prob draw | 0.0188 |
| Raw ev draw | 0.0214 |
| Raw edge prob away | 0.0484 |
| Raw ev away | 0.1381 |
| Elo home rating | 1,515.0066 |
| Elo away rating | 1,527.1311 |
| Elo rating diff | 47.8755 |
| Elo home expectancy | 0.5685 |

</details>


---

## 2026-11-07 — Samsunspor vs Torku Konyaspor

The model's most likely 1X2 outcome is **Samsunspor win** at **41.4%**. Expected goals are 1.41 for Samsunspor and 1.08 for Torku Konyaspor (2.49 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 48.5%; Under 3.5 goals: 73.2%; Double Chance 1X: 70.1%; Double Chance X2: 58.6%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 53.9%; BTTS No (at least one team does not score): 46.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Samsunspor win | 41.4% | 2.41 |
| Draw | 28.7% | 3.48 |
| Torku Konyaspor win | 29.9% | 3.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Samsunspor expected goals | 1.41 |
| Torku Konyaspor expected goals | 1.08 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 74.8% |
| Under 1.5 | 25.2% |
| Over 2.5 | 48.5% |
| Under 2.5 | 51.5% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.71% |
| 2 | 1-0 | 9.04% |
| 3 | 0-0 | 8.61% |
| 4 | 2-1 | 8.58% |
| 5 | 0-1 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Samsunspor win | 41.4% | 40.6% | 2.37 | -1.8% |
| Draw | 28.7% | 28.6% | 3.48 | -0.1% |
| Torku Konyaspor win | 29.9% | 30.8% | 3.18 | -5.0% |
| Over 2.5 | 48.5% | 48.5% | 1.98 | -4.0% |
| Under 2.5 | 51.5% | 51.5% | 1.90 | -2.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T13:00:00+00:00 |
| Fixture id | 605767f0e7114a23442d92831c12c767 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:31:26Z |
| Market best draw last update utc | 2026-11-05T12:29:41Z |
| Market best away last update utc | 2026-11-05T12:29:41Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Samsunspor |
| Matched away-team name | Konyaspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4120 |
| Dc lambda away | 1.0826 |
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
| P btts yes | 53.9% |
| P btts no | 46.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.61 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.96 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.74 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 8.02 |
| Fair Under 4.5 odds | 1.14 |
| Score matrix json | [[0.0861132617839413,0.07585233457263066,0.05037799483172484,0.019110318422900393,0.005436961188776766,0.0012374695727870963,0.00023470999246400772,3.815766933280561e-05,5.428003935508338e-06,6.863504853313315e-07,7.810777126921753e-08,8.080716330307345e-09,7.663319206784809e-10,6.708445013030329e-11,5.4530832679348605e-12,4.137130030082115e-13],[0.0904448781842402,0.13714302674215906,0.07477812169468244,0.028366228577082292,0.008070304242589369,0.001836826785512851,0.00034838965778723224,5.663899189487247e-05,8.05700862458802e-06,1.0187781448774552e-06,1.1593856493851233e-07,1.1994538312735811e-08,1.137497866170097e-09,9.957619775103943e-11,8.094234905198753e-12,6.14091160018513e-13],[0.07540826750396061,0.08581580163324257,0.05281776821114033,0.021052577614903995,0.005989541612178512,0.001363238625891431,0.00025856452121806743,4.203578807300752e-05,5.979673996920779e-06,7.561070696838693e-07,8.60461809470364e-08,8.901992314474385e-09,8.44217342790545e-10,7.390251495908985e-11,6.007302243648821e-12,4.557603339402388e-13],[0.037310526967390165,0.04245997006756765,0.024160058898584465,0.009913328832115816,0.0029635073346799094,0.0006745036479141852,0.00012793263737574055,2.079848080863375e-05,2.9586250328134977e-06,3.741069003102699e-07,4.2573957218904625e-08,4.4045306344593026e-09,4.177021297150308e-10,3.656551023658321e-11,2.9722949456589845e-12,2.2550124532765462e-13],[0.013845385943702054,0.015756268284747636,0.00896544131273827,0.0034009380258294883,0.001046601866614339,0.0002502983496847688,4.747391375122969e-05,7.718009292388115e-06,1.0979020874672568e-06,1.3882554978451083e-07,1.5798567234431812e-08,1.634456318139041e-09,1.5500309605558577e-10,1.356892122955977e-11,1.1029747903890879e-12,8.368018428352982e-14],[0.004110254719213289,0.004677534908590505,0.002661554370196129,0.0010096303293572093,0.00028724382264342876,7.071694189516492e-05,1.4093495033576623e-05,2.291231479278504e-06,3.2593220980590407e-07,4.1212890234289324e-08,4.6900921213879e-09,4.852180952048395e-10,4.601548917781848e-11,4.028181138843637e-12,3.274381339605938e-13,2.4841985175030063e-14],[0.0010168365791986625,0.0011571761169205253,0.000658442365746979,0.0002497726103347927,7.106129570203282e-05,1.6173775787771696e-05,3.3182029587371548e-06,5.668281259191098e-07,8.063242205415694e-08,1.0195663575017016e-08,1.1602826478237042e-09,1.2003818298341748e-10,1.138377930375122e-11,9.96532382888017e-13,8.100497287414128e-14,6.145662726887233e-15],[0.00021561888484079283,0.000245377702768554,0.00013962185422772782,5.296395980030921e-05,1.5068456080414677e-05,3.429628290686237e-06,6.50495210519255e-07,1.1439020585875669e-07,1.7098001076073345e-08,2.1619773080837962e-09,2.460364386389677e-10,2.5453941845401266e-11,2.4139157156235437e-12,2.113134062067138e-13,1.7176999996838816e-14,1.3031798529743476e-15],[4.0006493073397734e-05,4.55280221555027e-05,2.5905804810097824e-05,9.827071930435623e-06,2.795840838584364e-06,6.363422227926746e-07,1.2069458643723353e-07,1.962176416599695e-08,3.019192770704781e-09,4.0113893671494335e-10,4.5650245735577156e-11,4.7227910898464046e-12,4.4788424923060706e-13,3.9207643282113787e-14,3.1870656037512134e-15,2.4179540581477947e-16],[6.598141857621112e-06,7.508789838884292e-06,4.272560825545807e-06,1.6207472752760811e-06,4.611090112413915e-07,1.0494987021923972e-07,1.9905768828543444e-08,3.2361542719205132e-09,4.603493460433817e-10,6.296334602127016e-11,7.5289477797015e-12,7.789147006098491e-13,7.386810452983029e-14,6.466390138315143e-15,5.2563244982546105e-16,3.987853634558735e-17],[9.793892282454625e-07,1.1145604389920883e-06,6.341937078436474e-07,2.405741582048793e-07,6.844429968341967e-08,1.5578139211990407e-08,2.9546948203457746e-09,4.803556369735587e-10,6.833153946576167e-11,8.640263683112155e-12,1.0635790514388682e-12,1.1561750019336e-13,1.096454538998182e-14,9.598327807674437e-16,7.8021778022356e-17,5.919334530516573e-18],[1.3215886878754377e-07,1.5039888388033738e-07,8.557815483732094e-08,3.246309811353567e-08,9.23587983229209e-09,2.102115478398482e-09,3.9870677949854356e-10,6.481923199407993e-11,9.220663958582088e-12,1.165917942993763e-12,1.3268330678905444e-13,1.4847946013110188e-14,1.479556721392181e-15,1.2951992004106003e-16,1.0528265603553397e-17,7.9875552330666645e-19],[1.634740195303667e-08,1.8603602093722622e-08,1.0585596777268658e-08,4.015525544153662e-09,1.1424329021092082e-09,2.600213439502354e-10,4.931806730535339e-11,8.0178201388648e-12,1.1405507733812157e-12,1.442183141641203e-13,1.6412272354007823e-14,1.6979477851360715e-15,1.7417501758245794e-16,1.602097697461481e-17,1.3022946645094108e-18,9.880212899441016e-20],[1.866547574253833e-09,2.12416067459399e-09,1.2086642295456428e-09,4.5849300612578545e-10,1.3044307397014831e-10,2.9689256445693315e-11,5.6311406032684436e-12,9.154753014574054e-13,1.3022817237160927e-13,1.6466857867651044e-14,1.8739544814750192e-15,1.938718047467278e-16,1.8385765125764858e-17,1.7409292968916707e-18,1.4869610192414762e-19,1.1281234457648679e-20],[1.9789950258283662e-10,2.2521276537846602e-10,1.281478453140258e-10,4.861142523317396e-11,1.3830142778111677e-11,3.147784264221477e-12,5.970380502122106e-13,9.706267832884888e-14,1.380735797474435e-14,1.7458879838158616e-15,1.9868481514329252e-16,2.0555133045323973e-17,1.9493388881064353e-18,1.7064449998436448e-19,1.5003999388630552e-20,1.1960856066481512e-21],[1.958335596972105e-11,2.2286168968442236e-11,1.268100646431319e-11,4.810395337594387e-12,1.3685765027249597e-12,3.1149234312164415e-13,5.908053588906761e-14,9.604940670796966e-15,1.3663218082501434e-15,1.7276620417988787e-16,1.9661067410215766e-17,2.0340550743075332e-18,1.928989050158398e-19,1.6886308170835662e-20,1.3726347069211542e-21,1.1264359307403466e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.17491151739652733, "-10": 9.098422025175603e-08, "-11": 9.295172686566475e-09, "-12": 8.721409219184969e-10, "-13": 7.56344453694423e-11, "-14": 6.067174427953374e-12, "-15": 4.137130030082115e-13, "-2": 0.08545811665496994, "-3": 0.02867984831675677, "-4": 0.007554291277485038, "-5": 0.0016309972818138933, "-6": 0.0002977190606397606, "-7": 4.701504047005491e-05, "-8": 6.537391905552636e-06, "-9": 8.116226472190594e-07, "0": 0.2871081400542654, "1": 0.2041257649264266, "10": 1.1408463435443157e-06, "11": 1.5202111511254792e-07, "12": 1.860452086828228e-08, "13": 2.104441346096612e-09, "14": 2.2018567155127887e-10, "15": 1.958335596972105e-11, "2": 0.12791792413787123, "3": 0.05599384742646317, "4": 0.01923723098921992, "5": 0.005417356856299025, "6": 0.001289811430715275, "7": 0.000265669543610792, "8": 4.8183112447040756e-05, "9": 7.802429626933446e-06} |
| Raw goal margin distribution | {"-1": 0.16524744830827248, "-10": 5.7723965843026726e-08, "-11": 5.616382834964436e-09, "-12": 5.016955745577153e-10, "-13": 4.122700823965792e-11, "-14": 2.8740805673340234e-12, "-2": 0.07822225964942962, "-3": 0.025230836878385586, "-4": 0.006364782362654472, "-5": 0.0013134100355835414, "-6": 0.00022885987767744115, "-7": 3.4471523845154526e-05, "-8": 4.569240072946974e-06, "-9": 5.405475454888418e-07, "0": 0.29027437946088963, "1": 0.21924174187146148, "10": 8.226401477676659e-07, "11": 1.0439887460992189e-07, "12": 1.2163673602945437e-08, "13": 1.3037420758042128e-09, "14": 1.1854798430049667e-10, "2": 0.13307641890328048, "3": 0.05598707487463562, "4": 0.018421502692157563, "5": 0.004958236067915063, "6": 0.0011268909869391328, "7": 0.0002213900508696039, "8": 3.8276037270005344e-05, "9": 5.906119983325844e-06} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Samsunspor", "away_goals": 2.0, "away_xg": 0.99, "date": "2026-11-01T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 5.0, "home_xg": 3.89, "source": "pipeline training history"}, {"away": "Amedspor", "away_goals": 2.0, "away_xg": 1.63, "date": "2026-10-24T00:00:00+00:00", "home": "Samsunspor", "home_goals": 1.0, "home_xg": 1.08, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 1.0, "away_xg": 1.07, "date": "2026-10-18T00:00:00+00:00", "home": "Kasimpasa", "home_goals": 4.0, "home_xg": 2.41, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 3.0, "away_xg": 2.02, "date": "2026-10-10T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 0.36, "date": "2026-09-20T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 1.0, "home_xg": 0.72, "source": "pipeline training history"}, {"away": "Corum", "away_goals": 5.0, "away_xg": 1.73, "date": "2026-09-12T00:00:00+00:00", "home": "Samsunspor", "home_goals": 1.0, "home_xg": 1.24, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 1.74, "date": "2026-09-06T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 2.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 2.0, "away_xg": 0.32, "date": "2026-08-22T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.85, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 3.0, "away_xg": 1.89, "date": "2026-08-17T00:00:00+00:00", "home": "Samsunspor", "home_goals": 3.0, "home_xg": 2.74, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 43.3% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 27.7% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 75.9% |
| Raw p btts yes | 51.2% |
| P home draw | 70.1% |
| P draw away | 58.6% |
| P home away | 71.3% |
| Raw p home draw | 72.3% |
| Raw p draw away | 56.7% |
| Raw p home away | 71.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0512 |
| Totals anchor target over 2 5 | 0.4847 |
| Totals anchor reference over odds | 1.97 |
| Totals anchor reference under odds | 1.86 |
| Totals anchor reference last update utc | 2026-11-05T12:31:26Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4555 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.18, "draw": 3.48, "home": 2.33}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.98, "under": 1.9}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.09, "draw": 3.32, "home": 2.37}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.97, "under": 1.86}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.37 |
| Reference draw odds | 3.32 |
| Reference away odds | 3.09 |
| Market reference 1x2 last update utc | 2026-11-05T12:31:26Z |
| Market reference home last update utc | 2026-11-05T12:31:26Z |
| Market reference draw last update utc | 2026-11-05T12:31:26Z |
| Market reference away last update utc | 2026-11-05T12:31:26Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.86 |
| Market reference over 2 5 last update utc | 2026-11-05T12:31:26Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:31:26Z |
| Market best over 2 5 last update utc | 2026-11-05T12:29:41Z |
| Market best under 2 5 last update utc | 2026-11-05T12:29:41Z |
| Home probability edge | +0.8% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0268 |
| Raw ev home | 0.0264 |
| Raw edge prob draw | 0.0045 |
| Raw ev draw | 0.0102 |
| Raw edge prob away | -0.0313 |
| Raw ev away | -0.1203 |
| Elo home rating | 1,436.0175 |
| Elo away rating | 1,425.6973 |
| Elo rating diff | 70.3203 |
| Elo home expectancy | 0.5998 |

</details>


---

## 2026-11-08 — Çaykur Rizespor vs Erzurum BB

The model's most likely 1X2 outcome is **Çaykur Rizespor win** at **49.0%**. Expected goals are 1.42 for Çaykur Rizespor and 0.93 for Erzurum BB (2.35 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 52.6%; Under 3.5 goals: 69.5%; Double Chance 1X: 75.8%; Double Chance X2: 51.0%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Çaykur Rizespor win | 49.0% | 2.04 |
| Draw | 26.8% | 3.73 |
| Erzurum BB win | 24.2% | 4.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Çaykur Rizespor expected goals | 1.42 |
| Erzurum BB expected goals | 0.93 |
| Expected total goals | 2.35 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 30.5% |
| Under 3.5 | 69.5% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.75% |
| 2 | 2-1 | 9.49% |
| 3 | 1-0 | 9.11% |
| 4 | 2-0 | 8.58% |
| 5 | 0-0 | 7.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Çaykur Rizespor win | 49.0% | 49.9% | 2.01 | -1.5% |
| Draw | 26.8% | 25.7% | 3.71 | -0.6% |
| Erzurum BB win | 24.2% | 24.5% | 3.82 | -7.6% |
| Over 2.5 | 52.6% | 52.6% | 1.86 | -2.1% |
| Under 2.5 | 47.4% | 47.4% | 2.03 | -3.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T10:30:00+00:00 |
| Fixture id | cf2febfddf729564889172cf83e8fbab |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:29:41Z |
| Market best draw last update utc | 2026-11-05T12:29:41Z |
| Market best away last update utc | 2026-11-05T12:31:26Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Rizespor |
| Matched away-team name | Erzurumspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4174 |
| Dc lambda away | 0.9324 |
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
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.57 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.28 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.67 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.07367761473247543,0.057663675658505595,0.038093858199036434,0.014052725062327291,0.003888010253100789,0.0008605661129024263,0.00015873029871885466,2.5095083029273902e-05,3.4715665355824514e-06,4.268839507339996e-07,4.724291324214077e-08,4.7530329916827546e-09,4.383453724699002e-10,3.7316415253232354e-11,2.9498417967239905e-12,2.176377910062803e-13],[0.09107019865236482,0.1275094786180247,0.06409068108208049,0.023642885307074507,0.006541349103400735,0.001447851987160234,0.0002670544133413824,4.222100462373766e-05,5.840706985486334e-06,7.182071976695543e-07,7.948342932790748e-08,7.996699101753147e-09,7.374903671869283e-10,6.278267894591718e-11,4.96293572703042e-12,3.661628124384844e-13],[0.0857718957471249,0.09492308676463501,0.05412944574277902,0.01988888358536295,0.005502718010894656,0.001217963004407496,0.00022465168988130454,3.551718138087498e-05,4.913323385948775e-06,6.041707329327235e-07,6.686310288851046e-08,6.726988497226889e-09,6.203921335235012e-10,5.281408662752894e-11,4.174924068468544e-12,3.080237227940614e-13],[0.04810206050725423,0.05323417447306297,0.02945692244723213,0.011198448060798838,0.0030860000517510416,0.0006830504283866239,0.00012598776190731037,1.9918524511418868e-05,2.7554594281022097e-06,3.3882726852538003e-07,3.749774903341465e-08,3.772587802876649e-09,3.4792445340083687e-10,2.96188672112674e-11,2.341354920576038e-12,1.7274394628273445e-13],[0.0202322235467301,0.022390843695816627,0.01238988587320939,0.00457059662531711,0.001303180661706027,0.0002872980661342732,5.299175411989881e-05,8.377937169142142e-06,1.1589746995329134e-06,1.4251424924925215e-07,1.577194059761358e-08,1.5867894009645758e-09,1.463406191823742e-10,1.2458001513862451e-11,9.847980659412076e-13,7.265788826259413e-14],[0.0068079057791402085,0.0075342561258528295,0.004169051189271888,0.0015379521241323986,0.00042550989938848325,9.705801105720225e-05,1.783110335284635e-05,2.8190775343768105e-06,3.899813847253882e-07,4.7954372332477405e-08,5.307072912413681e-09,5.339360109458203e-10,4.924190090889234e-11,4.191971302949989e-12,3.313729916497884e-13,2.444852669112498e-14],[0.0019089836645406369,0.002112657303922723,0.0011690306645164635,0.0004312523670363002,0.00011931590615161706,2.6409196190374867e-05,5.019906821480396e-06,7.904887548074268e-07,1.0935346596552407e-07,1.3446736249860416e-08,1.4881397929104874e-09,1.497193345314319e-10,1.3807768129522499e-11,1.1754576222359689e-12,9.291926892814582e-14,6.855535254093611e-15],[0.0004588218567027612,0.0005077745633804186,0.00028097507066147476,0.00010365097168008996,2.867743009620289e-05,6.347417557923972e-06,1.1707729016478385e-06,1.9075078997979794e-07,2.6282969950535114e-08,3.2319063841952246e-09,3.576725539873878e-10,3.5984856408157655e-11,3.3186799488057456e-12,2.8251978198016644e-13,2.2333031070401552e-14,1.647719397709654e-15],[9.64926062942363e-05,0.00010678761335085195,5.909050860538429e-05,2.1798334704925068e-05,6.031011669080183e-06,1.3348946970472312e-06,2.462195882962296e-07,3.892704204300449e-08,5.549490861528533e-09,6.796866054966684e-10,7.522038549379176e-11,7.56780116557618e-12,6.979355343225129e-13,5.941536937418881e-14,4.696751784929156e-15,3.4652389986202024e-16],[1.8038127547637903e-05,1.9962654799236852e-05,1.1046257034746346e-05,4.0749354467071435e-06,1.1274248038904826e-06,2.4954244405606556e-07,4.602777880070148e-08,7.2769404453936955e-09,1.0066666407194649e-09,1.2756598623894428e-10,1.406154274227076e-11,1.4147090427173995e-12,1.3047062020222677e-13,1.1106985832609375e-14,8.780010304396624e-16,6.477845862050664e-17],[3.034809112621712e-06,3.3585995296268364e-06,1.8584679269439903e-06,6.855839772921152e-07,1.8968260755483082e-07,4.198405190379153e-08,7.74390369339622e-09,1.2243025290381762e-09,1.6936575520710167e-10,2.0826195310044598e-11,2.3752080710539523e-12,2.3801649496093736e-13,2.195091625078205e-14,1.868685190829421e-15,1.4771852128401574e-16,1.0898595544571675e-17],[4.641716591061909e-07,5.136951478946233e-07,2.842512029694053e-07,1.0485952835478037e-07,2.9011805153126655e-08,6.421427610433202e-09,1.18442395944207e-09,1.8725610575902887e-10,2.590435861790978e-11,3.185350139397039e-12,3.5252021075663686e-13,3.6549636269200345e-14,3.3573753198020683e-15,2.858139254185709e-16,2.2593431270502972e-17,1.6669315888144807e-18],[6.507846491438607e-08,7.202182856946582e-08,3.985299743404724e-08,1.4701666943897714e-08,4.067554980406119e-09,9.003062622361499e-10,1.660603175056728e-10,2.6253950816621476e-11,3.6318802761278525e-12,4.4659705783407264e-13,4.942454740023094e-14,4.972523671185033e-15,4.725930565439184e-16,4.0072096502428065e-17,3.1676768613239314e-18,2.337095485886336e-19],[8.42236141775979e-09,9.320961565058163e-09,5.157717663011442e-09,1.9026686110057075e-09,5.264171208810444e-10,1.165163428055763e-10,2.149128767896835e-11,3.397748590298964e-12,4.700327266757652e-13,5.779794950810597e-14,6.396453906243343e-15,6.435368684891663e-16,5.934976862345019e-17,5.2067580996313824e-18,4.099561877472536e-19,3.024635396032273e-20],[1.0121520616699775e-09,1.1201407772559813e-09,6.1982552246223e-10,2.2865202070803655e-10,6.326185113293828e-11,1.400227925866876e-11,2.5827021726165957e-12,4.083223302974909e-13,5.648589151660711e-14,6.945832748470065e-15,7.686898824989166e-16,7.733664418965309e-17,7.132321648557225e-18,6.071757410315903e-19,4.9462731882216986e-20,3.634836834998152e-21],[1.1352576339581085e-10,1.256380752107044e-10,6.952133802270072e-11,2.5646240506634888e-11,7.0956234894680024e-12,1.5705342135043842e-12,2.896829902085603e-13,4.579855736508258e-14,6.335613193273989e-15,7.790637346414808e-16,8.621837471865925e-17,8.674291050313817e-18,7.999808433932119e-19,6.810250369129198e-20,5.383464903765688e-21,4.0931942038376974e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1450351870129015, "-10": 5.589063259122132e-08, "-11": 5.54575145830605e-09, "-12": 5.054757194305686e-10, "-13": 4.258737470305684e-11, "-14": 3.3160046091624747e-12, "-15": 2.176377910062803e-13, "-2": 0.0679784354390762, "-3": 0.02194680666270567, "-4": 0.005581640908559453, "-5": 0.0011660411414732663, "-6": 0.00020621977396872448, "-7": 3.157909572616542e-05, "-8": 4.260560051100866e-06, "-9": 5.134550892425756e-07, "0": 0.2679204421639218, "1": 0.22047393431292203, "10": 3.5903247589467346e-06, "11": 5.415869529828656e-07, "12": 7.50448982424131e-08, "13": 9.612023533038473e-09, "14": 1.137790136880682e-09, "15": 1.1352576339581085e-10, "2": 0.1530598252103691, "3": 0.07512326736261107, "4": 0.02904544979774288, "5": 0.009224507108440099, "6": 0.002480119945523643, "7": 0.0005773712450830126, "8": 0.00011842277524859587, "9": 2.1696220656261174e-05} |
| Raw goal margin distribution | {"-1": 0.1500073551459286, "-10": 1.4705269277976859e-08, "-11": 1.2341527022147514e-09, "-12": 9.507708294642266e-11, "-13": 6.7445623071577e-12, "-14": 4.1042367881026086e-13, "-2": 0.06302356368526614, "-3": 0.017748622553236153, "-4": 0.0038904660062827074, "-5": 0.0006957249511805342, "-6": 0.00010488482877250219, "-7": 1.3653482542821655e-05, "-8": 1.56295682498301e-06, "-9": 1.5959829806155396e-07, "0": 0.2940869931389408, "1": 0.2343776321063772, "10": 9.696250065033579e-07, "11": 1.237122788230369e-07, "12": 1.4488814081586023e-08, "13": 1.5625137386137126e-09, "14": 1.4454915756562045e-10, "2": 0.145656249122267, "3": 0.06235968337349314, "4": 0.020780402500349005, "5": 0.0056494086671520114, "6": 0.0012947656497722024, "7": 0.00025623297407417013, "8": 4.459145484337731e-05, "9": 6.9222295823177554e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.9% |
| Raw p btts yes | 47.2% |
| P home draw | 75.8% |
| P draw away | 51.0% |
| P home away | 73.2% |
| Raw p home draw | 76.5% |
| Raw p draw away | 53.0% |
| Raw p home away | 70.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1870 |
| Totals anchor target over 2 5 | 0.5262 |
| Totals anchor reference over odds | 1.83 |
| Totals anchor reference under odds | 2.02 |
| Totals anchor reference last update utc | 2026-11-05T12:31:26Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4266 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.82, "draw": 3.65, "home": 1.94}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:26Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.02}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.77, "draw": 3.71, "home": 2.01}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:41Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.86, "under": 2.03}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.94 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.82 |
| Market reference 1x2 last update utc | 2026-11-05T12:31:26Z |
| Market reference home last update utc | 2026-11-05T12:31:26Z |
| Market reference draw last update utc | 2026-11-05T12:31:26Z |
| Market reference away last update utc | 2026-11-05T12:31:26Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-11-05T12:31:26Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:31:26Z |
| Market best over 2 5 last update utc | 2026-11-05T12:29:41Z |
| Market best under 2 5 last update utc | 2026-11-05T12:29:41Z |
| Home probability edge | -0.8% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0281 |
| Raw ev home | -0.0544 |
| Raw edge prob draw | 0.0374 |
| Raw ev draw | 0.0911 |
| Raw edge prob away | -0.0092 |
| Raw ev away | -0.1004 |
| Elo home rating | 1,458.4916 |
| Elo away rating | 1,419.5564 |
| Elo rating diff | 98.9351 |
| Elo home expectancy | 0.6387 |

</details>


---
