# Primeira Liga — football model report

Fixtures in this report: **9**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,620 |
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
| Training sha256 | b3df8a6ba2e5ca811847821ea9d38323a7d64bb77cbc57ee92f21ada8c933425 |
| Training as of utc | 2026-11-06T12:16:33.661378+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-06', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1620, 'tune_start_date': '2025-11-07', 'audit_start_date': '2026-05-08', 'training_shot_matches': 1314, 'tuning_matches': 198, 'audit_matches': 105, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8711307065798971, 'audit_candidate_poisson_score': 0.8646870750778988, 'audit_gain': 0.006443631501998337, 'audit_gain_lower95': -0.00293184513832055, 'audit_baseline_briers': [0.5561730451150284, 0.1869297801463111, 0.22413333341424527, 0.24642443911265677], 'audit_candidate_briers': [0.5573865705936081, 0.18683207454428277, 0.2222644657407454, 0.24657748450017997], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1467.258 |
| Base scoring parameter | 0.087 |
| Home-advantage parameter | 0.174 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1620, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 30.00 |
| Over 1 5 in window quote fixtures | 4 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 4.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 4.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 3, 'ANCHORED_MAIN': 4, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 9} |
| Legacy comparison status | {'None': 9} |
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

## 2026-11-06 — Famalicão vs Arouca

The model's most likely 1X2 outcome is **Famalicão win** at **43.2%**. Expected goals are 1.47 for Famalicão and 1.00 for Arouca (2.47 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 43.2%; Under 3.5 goals: 77.1%; Double Chance 1X: 71.4%; Double Chance X2: 56.8%; Double Chance 12 (either team wins): 71.8%; Under 4.5 goals: 90.2%; BTTS Yes (both teams score): 48.5%; BTTS No (at least one team does not score): 51.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Famalicão win | 43.2% | 2.32 |
| Draw | 28.2% | 3.55 |
| Arouca win | 28.6% | 3.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Famalicão expected goals | 1.47 |
| Arouca expected goals | 1.00 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 69.2% |
| Under 1.5 | 30.8% |
| Over 2.5 | 43.2% |
| Under 2.5 | 56.8% |
| Over 3.5 | 22.9% |
| Under 3.5 | 77.1% |
| Over 4.5 | 9.8% |
| Under 4.5 | 90.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.28% |
| 2 | 1-0 | 11.76% |
| 3 | 0-1 | 10.01% |
| 4 | 0-0 | 8.99% |
| 5 | 2-0 | 8.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Famalicão win | 43.2% | 40.8% | 2.39 | +3.1% |
| Draw | 28.2% | 29.6% | 3.27 | -7.8% |
| Arouca win | 28.6% | 29.6% | 3.26 | -6.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T20:45:00+00:00 |
| Fixture id | d98d64a216d4db8db11c9b5017f76ca6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T12:16:29Z |
| Market best draw last update utc | 2026-11-06T12:16:29Z |
| Market best away last update utc | 2026-11-06T12:16:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Famalicao |
| Matched away-team name | Arouca |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4703 |
| Dc lambda away | 0.9993 |
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
| P btts yes | 48.5% |
| P btts no | 51.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.13 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.25 |
| Fair Over 2.5 odds | 2.32 |
| Fair Under 2.5 odds | 1.76 |
| Fair Over 3.5 odds | 4.38 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 10.17 |
| Fair Under 4.5 odds | 1.11 |
| Score matrix json | [[0.08985327213630474,0.10012740439936588,0.046220542033714396,0.015260628743742032,0.003778949457436892,0.0007486170716376866,0.0001235853875659534,1.7487500159744696e-05,2.1651918918378185e-06,2.382936833309287e-07,2.360321584268459e-08,2.125382695568649e-09,1.754343135558007e-10,1.3366873473714142e-11,9.457153738427055e-13,6.244933781579412e-14],[0.11762643177643635,0.13280734888634702,0.06736061745704221,0.02224044396128731,0.005507342787244402,0.0010910150761021897,0.00018011013391054962,2.548582852363106e-05,3.155494425850549e-06,3.47283024798277e-07,3.439871371424729e-08,3.097477537186548e-09,2.556734119572031e-10,1.9480534217940777e-11,1.378261022430133e-12,9.10120429134494e-14],[0.08166819698805115,0.08089312540924026,0.05045081467751712,0.016206322685033483,0.004013129166959685,0.0007950085172906337,0.0001312439155477186,1.8571192268838538e-05,2.299367808717002e-06,2.53060630116558e-07,2.50658959584416e-08,2.257091655394384e-09,1.8630589494410882e-10,1.4195212297124982e-11,1.0043209080082609e-12,6.631929372663939e-14],[0.03967370303090024,0.039297179968318934,0.019462115147906394,0.008091990179158588,0.0019495434044894783,0.00038620825468498667,6.375715789115025e-05,9.02172441876548e-06,1.1170129740368477e-06,1.229346631654638e-07,1.217679524141023e-08,1.0964755847706718e-09,9.050579076699969e-11,6.895911234811734e-12,4.8789040191341e-13,3.22173387140492e-14],[0.014454856084440868,0.014317672351481871,0.007090895279996758,0.0023411997256512287,0.00073007089838806,0.0001407124698127251,2.322950648069713e-05,3.2870067108475276e-06,4.069764239446026e-07,4.4790446267694184e-08,4.436536278128595e-09,3.9949375952173547e-10,3.2975197181028366e-11,2.5124804809030893e-12,1.7775969989858373e-13,1.1738178162309526e-14],[0.004213226363249433,0.004173240761391108,0.0020668173213347447,0.0006824007342669885,0.00016898110345356845,4.215554432448478e-05,6.770815879315097e-06,9.580796411544697e-07,1.1862337394213519e-07,1.3055286606408013e-08,1.2931385479959239e-09,1.16442365786149e-10,9.611439178976172e-12,7.323247590603717e-13,5.181247392301452e-14,3.421383194758682e-15],[0.0010233744450240162,0.001013662115426051,0.0005020209803196247,0.00016575218431317794,4.1044778527629166e-05,8.131048656102404e-06,1.6903703778188576e-06,2.3271339741145005e-07,2.881310402256258e-08,3.1710726017479115e-09,3.140977554488316e-10,2.82833465828261e-11,2.334576969674322e-12,1.7787851381969176e-13,1.2585025625205691e-14,8.310391672025557e-16],[0.00021306276224322392,0.0002110406912583358,0.00010451890536355953,3.450898975377961e-05,8.545370593607905e-06,1.6928541601041997e-06,2.7946468948595906e-07,4.979840883295161e-08,5.9987813470410255e-09,6.602055494813156e-10,6.539398723089496e-11,5.888487813742466e-12,4.860502626842057e-13,3.7033646562528357e-14,2.6201556386774494e-15,1.7301927105706622e-16],[3.881401696711445e-05,3.84456527504403e-05,1.9040392246179324e-05,6.286563169082253e-06,1.5567251438895048e-06,3.0839021047763764e-07,5.0910572477393845e-08,7.203915138074039e-09,1.123220872431572e-09,1.2027080250700105e-10,1.191293731107133e-11,1.0727161494899637e-12,8.854462855953693e-14,6.746484326487746e-15,4.773183466945381e-16,3.1519223968290215e-17],[6.285171133037774e-06,6.2255217506240425e-06,3.083219235174651e-06,1.0179859866040476e-06,2.5208119903534385e-07,4.993776475770911e-08,8.24397177886666e-09,1.1665332013699814e-09,1.4443277804680633e-10,2.0017499170759924e-11,1.929067268679575e-12,1.7370540602458515e-13,1.4338071317881608e-14,1.0924612253933615e-15,7.729237343446388e-17,5.10392203901738e-18],[9.159845162261026e-07,9.072913701626286e-07,4.493403631772667e-07,1.4835863363576867e-07,3.673765920777476e-08,7.2778001306218655e-09,1.20145503468528e-09,1.7000751888869006e-10,2.1049257932051416e-11,2.316610007140656e-12,2.889611732988727e-13,2.5315374702675115e-14,2.0895932730756735e-15,1.5921246149968582e-16,1.1264389750055379e-17,7.438323413646627e-19],[1.2135745843182175e-07,1.202057161333969e-07,5.9532452219491884e-08,1.9655819935290732e-08,4.8673191208064534e-09,9.642251710388475e-10,1.5917903288392597e-10,2.252404930558739e-11,2.78878561728774e-12,3.069242958413918e-13,3.040114324829895e-14,3.4473374282318142e-15,2.7684717840153915e-16,2.1093827827878667e-17,1.4924026406956736e-18,9.854926677071083e-20],[1.473860065477314e-08,1.4598724045514465e-08,7.230087467227146e-09,2.3871567871630338e-09,5.911253721682853e-10,1.171030600085102e-10,1.9331949009192587e-11,2.7354970360554665e-12,3.386919770412829e-13,3.7275291408604165e-14,3.6921530458464194e-15,3.3246478976995747e-16,3.4558188990366855e-17,2.5617997332261496e-18,1.812490704862583e-19,1.1968595144650379e-20],[1.6522810602499098e-09,1.6366000958447007e-09,8.105339757733962e-10,2.676138691632945e-10,6.626852029880653e-11,1.3127919853551948e-11,2.167221566944449e-12,3.0666479463777706e-13,3.796929925926693e-14,4.178772425711051e-15,4.1391138087593133e-16,3.7271196106325614e-17,3.076456168552478e-18,2.9518476810356613e-19,2.031905289837403e-20,1.3417476691656272e-21],[1.7199939299380564e-10,1.703670336911786e-10,8.437508314281224e-11,2.7858107291896423e-11,6.898430019084295e-12,1.3665921013103784e-12,2.2560374440238926e-13,3.1923236184944093e-14,3.952533610720133e-15,4.350024568900173e-16,4.308740684416009e-17,3.87986236764796e-18,3.2025337958122013e-19,2.4401078202012745e-20,2.174040073727637e-21,1.3967344309595586e-22],[1.671116319643926e-11,1.655256599312001e-11,8.197736977847629e-12,2.706645466566046e-12,6.702395156259942e-13,1.3277572223051426e-13,2.191926916028055e-14,3.1016063508101355e-15,3.8402132157835145e-16,4.226408547966743e-17,4.18629784065613e-18,3.7696070943589504e-19,3.111526382297011e-20,2.370766506237596e-21,1.6773333997282662e-22,1.394808867856882e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.18579161006602732, "-10": 2.6894076367133157e-08, "-11": 2.395750948403053e-09, "-12": 1.959513860204638e-10, "-13": 1.4811453789870916e-11, "-14": 1.036727416756155e-12, "-15": 6.244933781579412e-14, "-2": 0.07288454048816657, "-3": 0.021630146073806807, "-4": 0.005010650525292009, "-5": 0.0009484615231521486, "-6": 0.00015149807391220388, "-7": 2.0908641296682103e-05, "-8": 2.538671008459293e-06, "-9": 2.750425596153314e-07, "0": 0.2819773936343575, "1": 0.22050027102672864, "10": 1.0436949649016312e-06, "11": 1.3679524479991715e-07, "12": 1.646228247922722e-08, "13": 1.830845830918936e-09, "14": 1.8855195898692565e-10, "15": 1.671116319643926e-11, "2": 0.1287814627017871, "3": 0.05623280706563989, "4": 0.019166234703136022, "5": 0.0053379534681602305, "6": 0.0012545112360421227, "7": 0.0002547449794841843, "8": 4.550913938284843e-05, "9": 7.254449769238727e-06} |
| Raw goal margin distribution | {"-1": 0.17011412694149683, "-10": 2.6443512285821218e-08, "-11": 2.3760489574666425e-09, "-12": 1.960313361113893e-10, "-13": 1.494669367424697e-11, "-14": 1.0552004486837592e-12, "-15": 6.402551706652768e-14, "-2": 0.0671381680931283, "-3": 0.020067542443002555, "-4": 0.004684737966746133, "-5": 0.0008939461992909431, "-6": 0.00014397513681896576, "-7": 2.003791811248855e-05, "-8": 2.453687425445712e-06, "-9": 2.681186898432303e-07, "0": 0.2503641213087209, "1": 0.24736531285287922, "10": 1.2573115785544793e-06, "11": 1.6622316177033673e-07, "12": 2.017781015666214e-08, "13": 2.2636331388428698e-09, "14": 2.3513011384883905e-10, "15": 2.0991272140646994e-11, "2": 0.145343040897931, "3": 0.06391919886725943, "4": 0.02195506943271144, "5": 0.006164151022680658, "6": 0.0014607024770468804, "7": 0.0002991157220671207, "8": 5.389125015567015e-05, "9": 8.664399872593712e-06} |
| Research history json | {"away": [{"away": "Nacional", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-11-01T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": 2.04, "date": "2026-10-24T00:00:00+00:00", "home": "Alverca", "home_goals": 0.0, "home_xg": 0.39, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 0.0, "away_xg": 1.45, "date": "2026-10-11T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.74, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 2.0, "away_xg": 2.08, "date": "2026-09-19T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 2.0, "away_xg": 1.16, "date": "2026-09-13T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.72, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": 1.08, "date": "2026-09-07T00:00:00+00:00", "home": "Estoril", "home_goals": 0.0, "home_xg": 0.87, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.67, "date": "2026-08-29T00:00:00+00:00", "home": "Arouca", "home_goals": 2.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": 0.54, "date": "2026-08-23T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.99, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 0.0, "away_xg": 0.49, "date": "2026-08-16T00:00:00+00:00", "home": "Arouca", "home_goals": 4.0, "home_xg": 2.14, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": 0.49, "date": "2026-08-08T00:00:00+00:00", "home": "Guimaraes", "home_goals": 0.0, "home_xg": 2.22, "source": "pipeline training history"}], "h2h": [{"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2026-03-06T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": null, "date": "2025-10-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2025-04-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2024-11-09T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2024-02-23T00:00:00+00:00", "home": "Arouca", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2023-09-22T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": null, "date": "2023-04-03T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Famalicao", "away_goals": 0.0, "away_xg": 0.17, "date": "2026-11-01T00:00:00+00:00", "home": "Sp Braga", "home_goals": 3.0, "home_xg": 1.15, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.65, "date": "2026-10-25T00:00:00+00:00", "home": "Rio Ave", "home_goals": 0.0, "home_xg": 0.58, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 4.0, "away_xg": 2.89, "date": "2026-10-12T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.36, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.45, "date": "2026-09-19T00:00:00+00:00", "home": "Nacional", "home_goals": 0.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "Sp Lisbon", "away_goals": 1.0, "away_xg": 2.28, "date": "2026-09-13T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.35, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": 1.81, "date": "2026-09-05T00:00:00+00:00", "home": "Estrela", "home_goals": 2.0, "home_xg": 0.94, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 0.0, "away_xg": 0.27, "date": "2026-08-30T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": 0.23, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 0.0, "away_xg": 1.05, "date": "2026-08-23T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": 1.36, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 2.0, "away_xg": 1.61, "date": "2026-08-16T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": 1.47, "date": "2026-08-07T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 1.22, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 48.7% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 26.3% |
| Raw p over 1 5 | 70.0% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 48.0% |
| P home draw | 71.4% |
| P draw away | 56.8% |
| P home away | 71.8% |
| Raw p home draw | 73.7% |
| Raw p draw away | 51.3% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9912 |
| Totals anchor target over 2 5 | 0.4317 |
| Totals anchor reference over odds | 2.22 |
| Totals anchor reference under odds | 1.71 |
| Totals anchor reference last update utc | 2026-11-06T12:16:29Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4368 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.29, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.23, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.81, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.29, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.26, "draw": 3.27, "home": 2.39}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.22, "under": 1.71}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.38, "under": 3.14}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.39 |
| Reference draw odds | 3.27 |
| Reference away odds | 3.26 |
| Market reference 1x2 last update utc | 2026-11-06T12:16:29Z |
| Market reference home last update utc | 2026-11-06T12:16:29Z |
| Market reference draw last update utc | 2026-11-06T12:16:29Z |
| Market reference away last update utc | 2026-11-06T12:16:29Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.26 |
| Reference Under 2.5 odds | 1.72 |
| Market reference over 2 5 last update utc | 2026-11-06T12:16:21Z |
| Market reference under 2 5 last update utc | 2026-11-06T12:16:21Z |
| Home probability edge | +2.4% |
| Draw probability edge | -1.4% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | 0.0786 |
| Raw ev home | 0.1629 |
| Raw edge prob draw | -0.0452 |
| Raw ev draw | -0.1813 |
| Raw edge prob away | -0.0334 |
| Raw ev away | -0.1424 |
| Market p home draw | 70.6% |
| Market reference home draw last update utc | 2026-11-06T12:16:22Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.8% |
| Market reference draw away last update utc | 2026-11-06T12:16:22Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.6% |
| Market reference home away last update utc | 2026-11-06T12:16:22Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.62 |
| Market reference dc home draw odds | 1.35 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 70.7% |
| Market over 1 5 odds | 1.38 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T12:16:29Z |
| Market reference over 1 5 odds | 1.38 |
| Market reference over 1 5 opposite odds | 3.14 |
| Market reference over 1 5 last update utc | 2026-11-06T12:16:29Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 77.3% |
| Market under 3 5 odds | 1.27 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T12:16:29Z |
| Market reference under 3 5 odds | 1.27 |
| Market reference under 3 5 opposite odds | 3.96 |
| Market reference under 3 5 last update utc | 2026-11-06T12:16:29Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,482.5254 |
| Elo away rating | 1,488.7246 |
| Elo rating diff | 53.8007 |
| Elo home expectancy | 0.5768 |
| Research p home | 0.4024 |
| Research p draw | 0.2768 |
| Research p away | 0.3207 |
| Research p over 1 5 | 0.6869 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4702946930990926, 0.9992910829352996], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "rotation": "schedule congestion only; rotation unconfirmed", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "recent": {"away": [], "home": []}, "rest_and_travel": {}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "schedules": {"away": [], "home": []}, "sources": [{"observed_at_utc": "2026-11-06T12:17:18.058894+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-06T12:17:18.060668+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/summary?event=401885399"}, {"observed_at_utc": "2026-11-06T12:17:18.061963+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/all/teams/12698/schedule"}, {"observed_at_utc": "2026-11-06T12:17:18.063325+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/all/teams/15784/schedule"}, {"observed_at_utc": "2026-11-06T12:17:18.064684+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/v2/sports/soccer/por.1/standings"}, {"observed_at_utc": "2026-11-06T12:17:18.065934+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:18.067298+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Famalic%C3%A3o%22+%22Arouca%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:18.149931+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Famalic%C3%A3o_vs_Arouca&d=2026-11-06"}, {"observed_at_utc": "2026-11-06T12:17:18.150337+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://geocoding-api.open-meteo.com/v1/search?name=Vila+Nova+de+Famalic%C3%A3o&count=10&language=en&format=json"}], "venue": {"address": {"city": "Vila Nova de Famalic\u00e3o", "country": "Portugal"}, "fullName": "Est\u00e1dio Municipal 22 de Junho", "id": "8157"}}, "form": {"away": {"all": {"goals_against": 0.6319445048828116, "goals_for": 1.2081082699386303, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 2.1060493109621126, "results": "WWWDLDWLWW", "xg_against": 1.023157856687065, "xg_for": 1.2317353640143311, "xg_matches": 10}, "venue": {"goals_against": 0.792388231715419, "goals_for": 0.8583663485684871, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 1.6443849010337144, "results": "WDDLW", "xg_against": 1.4009952478886567, "xg_for": 1.3739582889860773, "xg_matches": 5}}, "home": {"all": {"goals_against": 1.5415943551474574, "goals_for": 1.5655575353063838, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 1.1025143978756544, "results": "LWLWDDDLLD", "xg_against": 1.3722444855381826, "xg_for": 0.8727767251907648, "xg_matches": 10}, "venue": {"goals_against": 1.8825279789738854, "goals_for": 0.7695192334124757, "last_match": "2026-10-12T00:00:00+00:00", "matches": 4, "points_per_game": 0.495233644025069, "results": "LDDL", "xg_against": 1.8678153299912186, "xg_for": 0.3735383586410355, "xg_matches": 4}}}, "goal_rates": [1.273340132946194, 1.1053356774598386], "h2h": [{"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2026-03-06T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": null, "date": "2025-10-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2025-04-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2024-11-09T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2024-02-23T00:00:00+00:00", "home": "Arouca", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2023-09-22T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": null, "date": "2023-04-03T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.19356176256016805, "-10": 7.896039064030497e-08, "-11": 7.85133173930294e-09, "-12": 7.16670037082592e-10, "-13": 6.021457118491241e-11, "-14": 4.319808590913089e-12, "-2": 0.08831069971507992, "-3": 0.029316065325949575, "-4": 0.0075900938552133975, "-5": 0.0016050051779433843, "-6": 0.000286314421642854, "-7": 4.4122504567075135e-05, "-8": 5.981130293254673e-06, "-9": 7.234014713429954e-07, "0": 0.27684922048221683, "1": 0.22298200039835347, "10": 3.250211926800539e-07, "11": 3.723025050140286e-08, "12": 3.914913018065334e-09, "13": 3.789262628807575e-10, "14": 3.1316113019495445e-11, "2": 0.11719627390859227, "3": 0.04481840514594542, "4": 0.013367435669573784, "5": 0.003256324175612412, "6": 0.0006691826290114242, "7": 0.00011879873897055789, "8": 1.8551762521323385e-05, "9": 2.5848273482314284e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:18.150809+00:00", "p_over_1_5": 0.6868872562836535, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Alverca vs Casa Pia

The model's most likely 1X2 outcome is **Alverca win** at **52.9%**. Expected goals are 1.43 for Alverca and 0.91 for Casa Pia (2.33 combined). The most likely exact score is 1-0 at 12.3%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 48.9%; Under 3.5 goals: 72.4%; Double Chance 1X: 78.6%; Double Chance X2: 47.1%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 87.2%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alverca win | 52.9% | 1.89 |
| Draw | 25.7% | 3.89 |
| Casa Pia win | 21.4% | 4.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alverca expected goals | 1.43 |
| Casa Pia expected goals | 0.91 |
| Expected total goals | 2.33 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 73.8% |
| Under 1.5 | 26.2% |
| Over 2.5 | 48.9% |
| Under 2.5 | 51.1% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 12.8% |
| Under 4.5 | 87.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.31% |
| 2 | 1-1 | 12.21% |
| 3 | 2-1 | 9.77% |
| 4 | 2-0 | 9.49% |
| 5 | 0-0 | 7.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alverca win | 52.9% | 54.3% | 1.79 | -5.3% |
| Draw | 25.7% | 25.7% | 3.64 | -6.3% |
| Casa Pia win | 21.4% | 20.0% | 4.63 | -1.1% |
| Over 2.5 | 48.9% | 48.9% | 1.96 | -4.2% |
| Under 2.5 | 51.1% | 51.1% | 1.88 | -3.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T18:00:00+00:00 |
| Fixture id | d9d924bf6388e1288f06e04041b3fe33 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T12:16:29Z |
| Market best draw last update utc | 2026-11-06T12:16:29Z |
| Market best away last update utc | 2026-11-06T12:16:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Alverca |
| Matched away-team name | Casa Pia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4250 |
| Dc lambda away | 0.9056 |
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
| Fair Under 0.5 odds | 14.17 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.82 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.62 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.80 |
| Fair Under 4.5 odds | 1.15 |
| Score matrix json | [[0.0705673417640601,0.06806856202175698,0.03242339390530974,0.011130546956594425,0.00286573351747421,0.0005902623563927956,0.00010131485454186481,1.4905768556741581e-05,1.9188617020954155e-06,2.1957376763989467e-07,2.2613081205715194e-08,2.1171242444874793e-09,1.8169559057444504e-10,1.4393961076859027e-11,1.0588430166365682e-12,7.269752173849635e-14],[0.1230893250457236,0.12207342177225453,0.05254478706728695,0.01803797040756169,0.004644157792581065,0.0009565688873000851,0.00016418908749042576,2.4156028735782204e-05,3.10967383126613e-06,3.5583742096507684e-07,3.6646365286731786e-08,3.430974652020243e-09,2.9445270737791886e-10,2.3326602453992827e-11,1.7159425385675324e-12,1.178123367104763e-13],[0.09485388404486698,0.097686467998391,0.0536152053775964,0.014616010232601503,0.0037631205886514427,0.0007750994335319022,0.0001330409867972481,1.9573419581240724e-05,2.5197416067821787e-06,2.883319613268583e-07,2.9694230443685934e-08,2.780088861921078e-09,2.385924628332197e-10,1.8901342692992798e-11,1.3904132857289413e-12,9.546230978210045e-14],[0.051239517102973184,0.052769662498638244,0.02717275100996814,0.009942507261072073,0.0020328158799649133,0.00041870421101761874,7.186796816005473e-05,1.0573447545092147e-05,1.361149777427331e-06,1.5575525043078988e-07,1.6040650775662248e-08,1.5017878521538414e-09,1.288862623084629e-10,1.0210395514522653e-11,7.510931792799327e-13,5.156818515154901e-14],[0.020759467095496014,0.021379398835461423,0.011008921675665207,0.003779225580465687,0.0010371137365119557,0.00016963618673255441,2.9116994159811095e-05,4.2837862026915364e-06,5.514639015773393e-07,6.310356106148988e-08,6.498799770077865e-09,6.084428047701935e-10,5.221770759620899e-11,4.1366972543820866e-12,3.043021289521189e-13,2.0892625523317236e-14],[0.006728486113136699,0.00692941622778087,0.0035681733194102058,0.00122490942178816,0.00031537210162062935,6.923677494013912e-05,9.43729865315651e-06,1.38844585190292e-06,1.787385575260912e-07,2.0452906249401173e-08,2.1063683284293915e-09,1.972063610160015e-10,1.692462136935843e-11,1.3407718946889248e-12,9.862934532151313e-14,6.771644958608055e-15],[0.0018173445544312546,0.001871615194740209,0.0009637532488380254,0.0003308444767407702,8.518108856326429e-05,1.754496353163036e-05,3.20985032476997e-06,3.7501519147850723e-07,4.827676519280348e-08,5.5242705669068e-09,5.689239669862493e-10,5.326486527064535e-11,4.571291069675051e-12,3.6213859411704626e-13,2.663949967544951e-14,1.8290016332264056e-15],[0.00042073670158105796,0.00043330099498409253,0.0002231202454512199,7.659439897669015e-05,1.9720426790729125e-05,4.061866016358288e-06,6.971939852827562e-07,1.0932995114701522e-07,1.117664061044276e-08,1.2789338000295027e-09,1.3171260933242024e-10,1.2331444617635657e-11,1.0583078051613248e-12,8.383935629184571e-14,6.167358411969351e-15,4.2343545282797106e-16],[8.522982071422272e-05,8.77750050780242e-05,4.5198097636978245e-05,1.551594350567787e-05,3.994822494604705e-06,8.228236591637451e-07,1.412325526757872e-07,2.077858920473706e-08,2.8510815021150947e-09,2.590772282813882e-10,2.66813948890596e-11,2.4980155283790224e-12,2.143843980223453e-13,1.698357495007646e-14,1.2493391942210492e-15,8.577651436862066e-17],[1.534688466773468e-05,1.5805182603387443e-05,8.138583254346371e-06,2.7938741803898774e-06,7.193266344926122e-07,1.481615201492753e-07,2.5431001486119185e-08,3.7414910580719125e-09,4.816527153723682e-10,5.87455623975174e-11,4.804378170753936e-12,4.4980449203087113e-13,3.860306877850349e-14,3.0581428403868044e-15,2.2496192487462847e-16,1.5445324913089176e-17],[2.4870893817203725e-06,2.5613603464212876e-06,1.3189246177556555e-06,4.5277038033127024e-07,1.1657282069738145e-07,2.4010797730012762e-08,4.121303778063649e-09,6.063395199610846e-10,7.805579959807066e-11,8.931861001330627e-12,9.804501520074876e-13,7.28945320304694e-14,6.255946046345637e-15,4.9559729878604e-16,3.6456937467143365e-17,2.5030424363145625e-18],[3.6641215503915414e-07,3.7735417603482707e-07,1.9431147713386735e-07,6.670470792662919e-08,1.7174171046950666e-08,3.5374073023373002e-09,6.071739158191188e-10,8.932938712506882e-11,1.1499624402018788e-11,1.3158925698697277e-12,1.3551885482633094e-13,1.3523546548144526e-14,9.216615572796905e-16,7.301421316597993e-17,5.3710434058559996e-18,3.687624497878178e-19],[4.948342936591131e-08,5.096113340933159e-08,2.6241482771531287e-08,9.008373924463245e-09,2.3193468563537427e-09,4.777217184974716e-10,8.199795548007566e-11,1.2063803990430236e-11,1.5530075735915478e-12,1.7770938037609073e-13,1.8301624518518913e-14,1.7134689708658573e-15,1.5673953732367703e-16,9.860463443196313e-18,7.253516111290538e-19,4.980083325818159e-20],[6.168614092424819e-09,6.352824970762912e-09,3.2712684327837683e-09,1.1229856752522764e-09,2.8913023787274075e-10,5.955288391978317e-11,1.0221881349089928e-11,1.5038761916304023e-12,1.935982313040495e-13,2.2153286508052986e-14,2.2814841324836747e-15,2.1360138082703636e-16,1.8331672851954272e-17,1.5478978897586226e-18,9.042247531566824e-20,6.2081817244167466e-21],[7.140534634021199e-10,7.353769590370942e-10,3.786686148864067e-10,1.2999221522863148e-10,3.3468530310696444e-11,6.893597553902071e-12,1.1832430543461094e-12,1.740825389742545e-13,2.2410137106962508e-14,2.5643735723783214e-15,2.640952444241111e-16,2.472561964190977e-17,2.1219992519822395e-18,1.68105205754246e-19,1.3180645789146299e-20,7.186336501732704e-22],[7.714550652058425e-11,7.944927221301836e-11,4.0910917173731e-11,1.4044207894133726e-11,3.6159011273700354e-12,7.44776269988269e-13,1.2783620477040993e-13,1.8807675242652342e-14,2.4211651744888524e-15,2.770519411901761e-16,2.8532543352852627e-17,2.6713272171837954e-18,2.2925833361343336e-19,1.816189110668186e-20,1.336018033155629e-21,9.776977672006905e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.13744163514278357, "-10": 2.629316978985709e-08, "-11": 2.431250280363194e-09, "-12": 2.0646417449931837e-10, "-13": 1.620536592520866e-11, "-14": 1.1766553533470445e-12, "-15": 7.269752173849635e-14, "-2": 0.05467374413538873, "-3": 0.016626140334147964, "-4": 0.003966489337397352, "-5": 0.0007754512775116635, "-6": 0.0001281530807973863, "-7": 1.8320440735928104e-05, "-8": 2.3059487268987585e-06, "-9": 2.5913334520645727e-07, "0": 0.25730814877753233, "1": 0.25206140516299697, "10": 2.8918422395085637e-06, "11": 4.207781649976255e-07, "12": 5.622896715945477e-08, "13": 6.944901968635644e-09, "14": 7.935027356151382e-10, "15": 7.714550652058425e-11, "2": 0.1599467656489722, "3": 0.07653850303405613, "4": 0.028733378167314947, "5": 0.008839481453699938, "6": 0.002298757714985234, "7": 0.0005171207225849102, "8": 0.00010242301274508344, "9": 1.8111861016885932e-05} |
| Raw goal margin distribution | {"-1": 0.16476974948315773, "-10": 1.1172002794031872e-08, "-11": 9.109271212479286e-10, "-12": 6.817667494899743e-11, "-13": 4.699112473094676e-12, "-14": 2.7831147108180775e-13, "-2": 0.06004061033083558, "-3": 0.01645762924069433, "-4": 0.003508691641738104, "-5": 0.0006100200487194102, "-6": 8.938688250853215e-05, "-7": 1.1308073616742387e-05, "-8": 1.2578473076485844e-06, "-9": 1.2479881793747407e-07, "0": 0.25694804714094416, "1": 0.2556814597943844, "10": 1.040039398300161e-06, "11": 1.3344252893655162e-07, "12": 1.57158662196159e-08, "13": 1.704551873642183e-09, "14": 1.588610266538809e-10, "2": 0.14867188555442207, "3": 0.06412729204172464, "4": 0.021513580929146126, "5": 0.0058857727029536155, "6": 0.0013571412292810666, "7": 0.000270166661481093, "8": 4.728930475540949e-05, "9": 7.383076220843724e-06} |
| Research history json | {"away": [{"away": "Sp Lisbon", "away_goals": 2.0, "away_xg": 2.65, "date": "2026-10-30T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.31, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 2.0, "away_xg": 0.79, "date": "2026-10-24T00:00:00+00:00", "home": "Estrela", "home_goals": 0.0, "home_xg": 1.69, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 0.61, "date": "2026-10-10T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.43, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 2.0, "away_xg": 2.17, "date": "2026-09-20T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 0.95, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 4.0, "away_xg": 2.6, "date": "2026-09-12T00:00:00+00:00", "home": "Casa Pia", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.21, "date": "2026-09-06T00:00:00+00:00", "home": "Guimaraes", "home_goals": 0.0, "home_xg": 2.48, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.28, "date": "2026-08-30T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.78, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.76, "date": "2026-08-24T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 2.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 7.0, "away_xg": 3.04, "date": "2026-08-17T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.12, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.65, "date": "2026-08-08T00:00:00+00:00", "home": "Maritimo", "home_goals": 1.0, "home_xg": 1.28, "source": "pipeline training history"}], "h2h": [{"away": "Casa Pia", "away_goals": 1.0, "away_xg": null, "date": "2026-04-12T00:00:00+00:00", "home": "Alverca", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 2.0, "away_xg": null, "date": "2025-11-29T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Alverca", "away_goals": 0.0, "away_xg": 0.56, "date": "2026-11-02T00:00:00+00:00", "home": "Benfica", "home_goals": 1.0, "home_xg": 1.6, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": 2.04, "date": "2026-10-24T00:00:00+00:00", "home": "Alverca", "home_goals": 0.0, "home_xg": 0.39, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 4.0, "away_xg": 2.89, "date": "2026-10-12T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.36, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 0.0, "away_xg": 0.29, "date": "2026-09-19T00:00:00+00:00", "home": "Alverca", "home_goals": 1.0, "home_xg": 3.3, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 3.0, "away_xg": 1.16, "date": "2026-09-12T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 2.2, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 2.0, "away_xg": 2.26, "date": "2026-09-05T00:00:00+00:00", "home": "Alverca", "home_goals": 1.0, "home_xg": 1.08, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 1.41, "date": "2026-08-29T00:00:00+00:00", "home": "Alverca", "home_goals": 1.0, "home_xg": 0.41, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 1.0, "away_xg": 0.41, "date": "2026-08-22T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 3.0, "home_xg": 2.12, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 2.0, "away_xg": 1.29, "date": "2026-08-15T00:00:00+00:00", "home": "Alverca", "home_goals": 2.0, "home_xg": 1.75, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 0.0, "away_xg": 1.66, "date": "2026-08-09T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.59, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 49.8% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 67.0% |
| Raw p under 3 5 | 79.3% |
| Raw p btts yes | 44.6% |
| P home draw | 78.6% |
| P draw away | 47.1% |
| P home away | 74.3% |
| Raw p home draw | 75.5% |
| Raw p draw away | 50.2% |
| Raw p home away | 74.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1372 |
| Totals anchor target over 2 5 | 0.4889 |
| Totals anchor reference over odds | 1.96 |
| Totals anchor reference under odds | 1.88 |
| Totals anchor reference last update utc | 2026-11-06T12:16:29Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4138 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 4.19, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.19, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.63, "draw": 3.64, "home": 1.79}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.96, "under": 1.88}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.96, "under": 1.88}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.3, "under": 3.52}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.79 |
| Reference draw odds | 3.64 |
| Reference away odds | 4.63 |
| Market reference 1x2 last update utc | 2026-11-06T12:16:29Z |
| Market reference home last update utc | 2026-11-06T12:16:29Z |
| Market reference draw last update utc | 2026-11-06T12:16:29Z |
| Market reference away last update utc | 2026-11-06T12:16:29Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.96 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-11-06T12:16:29Z |
| Market reference under 2 5 last update utc | 2026-11-06T12:16:29Z |
| Market best over 2 5 last update utc | 2026-11-06T12:16:29Z |
| Market best under 2 5 last update utc | 2026-11-06T12:16:29Z |
| Home probability edge | -1.3% |
| Draw probability edge | -0.0% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0450 |
| Raw ev home | -0.1094 |
| Raw edge prob draw | -0.0005 |
| Raw ev draw | -0.0647 |
| Raw edge prob away | 0.0455 |
| Raw ev away | 0.1366 |
| Market p home draw | 78.6% |
| Market reference home draw last update utc | 2026-11-06T12:16:22Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.0% |
| Market reference draw away last update utc | 2026-11-06T12:16:22Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.4% |
| Market reference home away last update utc | 2026-11-06T12:16:22Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.05 |
| Market reference dc home draw odds | 1.20 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 74.9% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T12:16:29Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.52 |
| Market reference over 1 5 last update utc | 2026-11-06T12:16:29Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.4% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T12:16:29Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.38 |
| Market reference under 3 5 last update utc | 2026-11-06T12:16:29Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,417.0742 |
| Elo away rating | 1,403.5352 |
| Elo rating diff | 73.5391 |
| Elo home expectancy | 0.6043 |
| Research p home | 0.4733 |
| Research p draw | 0.2644 |
| Research p away | 0.2624 |
| Research p over 1 5 | 0.7046 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4250484136365722, 0.9056027725313941], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:18.180744+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T12:17:18.065934+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:18.283769+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Alverca%22+%22Casa+Pia%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:18.367210+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Alverca_vs_Casa+Pia&d=2026-11-07"}]}, "form": {"away": {"all": {"goals_against": 1.6404619578729738, "goals_for": 0.6273910578083026, "last_match": "2026-10-30T00:00:00+00:00", "matches": 10, "points_per_game": 0.8786878561846695, "results": "LWLWLDLLLL", "xg_against": 1.7424276306361413, "xg_for": 0.7986589891384444, "xg_matches": 10}, "venue": {"goals_against": 0.7157020266306037, "goals_for": 0.9685668669792039, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 1.6490589562063098, "results": "WWDLL", "xg_against": 1.6257944158120676, "xg_for": 0.9612876162123404, "xg_matches": 5}}, "home": {"all": {"goals_against": 1.2097349947013118, "goals_for": 1.2751965627375945, "last_match": "2026-11-02T00:00:00+00:00", "matches": 10, "points_per_game": 1.1634978383066994, "results": "LLWWWLDLDL", "xg_against": 1.522332345560108, "xg_for": 1.3567986568754096, "xg_matches": 10}, "venue": {"goals_against": 1.1195224506526886, "goals_for": 0.8897994815892832, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 0.9956615910184449, "results": "LWLDD", "xg_against": 1.4696091377324454, "xg_for": 1.3868989962085467, "xg_matches": 5}}}, "goal_rates": [1.4521478444278173, 1.0088846406783936], "h2h": [{"away": "Casa Pia", "away_goals": 1.0, "away_xg": null, "date": "2026-04-12T00:00:00+00:00", "home": "Alverca", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 2.0, "away_xg": null, "date": "2025-11-29T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.1666052565120134, "-10": 2.933355147855588e-08, "-11": 2.6611160749334905e-09, "-12": 2.216638438311864e-10, "-13": 1.7063743292062122e-11, "-14": 1.2162749175364306e-12, "-15": 7.452641253833249e-14, "-2": 0.06893457658957297, "-3": 0.02080802673643348, "-4": 0.00490511716897166, "-5": 0.0009451034249665025, "-6": 0.0001536897558518358, "-7": 2.1596832795348244e-05, "-8": 2.670116927807393e-06, "-9": 2.945825892809027e-07, "0": 0.26435971225983385, "1": 0.23980488388799506, "10": 1.119587107372762e-06, "11": 1.461929346351211e-07, "12": 1.7527773392455236e-08, "13": 1.9421175953518674e-09, "14": 1.9925181623425003e-10, "15": 1.757316871092958e-11, "2": 0.14281563680739112, "3": 0.062049583354087716, "4": 0.02105361527150745, "5": 0.00583883170754958, "6": 0.0013666612024711762, "7": 0.00027642373768354823, "8": 4.919091187012429e-05, "9": 7.811438043969248e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:18.367616+00:00", "p_over_1_5": 0.7046120005469835, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Nacional vs Académico de Viseu

The model's most likely 1X2 outcome is **Académico de Viseu win** at **43.7%**. Expected goals are 0.92 for Nacional and 1.60 for Académico de Viseu (2.51 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 45.2%; Under 3.5 goals: 75.4%; Double Chance 1X: 56.3%; Double Chance X2: 71.5%; Double Chance 12 (either team wins): 72.3%; Under 4.5 goals: 89.1%; BTTS Yes (both teams score): 49.5%; BTTS No (at least one team does not score): 50.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nacional win | 28.5% | 3.51 |
| Draw | 27.7% | 3.60 |
| Académico de Viseu win | 43.7% | 2.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nacional expected goals | 0.92 |
| Académico de Viseu expected goals | 1.60 |
| Expected total goals | 2.51 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 70.9% |
| Under 1.5 | 29.1% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 24.6% |
| Under 3.5 | 75.4% |
| Over 4.5 | 10.9% |
| Under 4.5 | 89.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.12% |
| 2 | 0-1 | 10.65% |
| 3 | 1-0 | 10.04% |
| 4 | 0-0 | 8.42% |
| 5 | 0-2 | 8.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nacional win | 28.5% | 31.2% | 3.05 | -13.0% |
| Draw | 27.7% | 29.4% | 3.23 | -10.4% |
| Académico de Viseu win | 43.7% | 39.4% | 2.44 | +6.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T15:30:00+00:00 |
| Fixture id | 406c4abcb4384570eada7fffa729be9d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T12:16:29Z |
| Market best draw last update utc | 2026-11-06T12:16:29Z |
| Market best away last update utc | 2026-11-06T12:16:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Nacional |
| Matched away-team name | Academico Viseu |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9184 |
| Dc lambda away | 1.5961 |
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
| P btts yes | 49.5% |
| P btts no | 50.5% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.87 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.44 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.06 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 9.15 |
| Fair Under 4.5 odds | 1.12 |
| Score matrix json | [[0.08422332938575659,0.10645584152189662,0.08252338832562132,0.04463872173661851,0.018109552201281243,0.00587751383860794,0.0015896384653372685,0.00036851593861932997,7.475190112753948e-05,1.3478317607565072e-05,2.1872158234263815e-06,3.2266726439896315e-07,4.3634460851837556e-08,5.44680986047894e-09,6.31349923892772e-10,6.830222108641841e-11],[0.10035371254688423,0.1311874553591748,0.0770616466702292,0.04168434515442657,0.016910986587034316,0.005488515485367736,0.001484429568813438,0.00034412601845886296,6.980450887315145e-05,1.2586266393776171e-05,2.0424567676662858e-06,3.013118005170701e-07,4.074655043903806e-08,5.086317290947085e-09,5.895645555454668e-10,6.37816955283607e-11],[0.043339452910615854,0.07032979927074615,0.05231496007001138,0.01946275076161032,0.007895873519352444,0.0025626313319115986,0.0006930919176959316,0.00016067516241499415,3.25922778252039e-05,5.876627422927965e-06,9.536392346619797e-07,1.4068486510392097e-07,1.902488698460857e-08,2.3748418107909204e-09,2.752723584825819e-10,2.9780178592767836e-11],[0.013490355784151246,0.021891693380326625,0.01776255002930557,0.008808471943710145,0.002457763904459247,0.0007976752379039108,0.00021574006898798502,5.001367024925272e-05,1.0145061696664965e-05,1.8292292454568405e-06,2.9684113899288715e-07,4.3791251532673056e-08,5.921913566951646e-09,7.392216284945314e-10,8.56845623116493e-11,9.269734100256643e-12],[0.003149376958420348,0.005110702476342558,0.004146737616127534,0.002243061879993305,0.0008342530044389351,0.00018622044182914788,5.03653730969056e-05,1.1675889295231044e-05,2.3684048115888643e-06,4.2704080822527123e-07,6.929873892234549e-08,1.0223241014845279e-08,1.3824941636769266e-09,1.725742153280887e-10,2.000340024787706e-11,2.1640561192855445e-12],[0.0005881876140216585,0.0009544909787624388,0.0007744578488398187,0.00041892133990779803,0.000169952847620803,5.056790452558738e-05,9.40639657376498e-06,2.1806260593166985e-06,4.423307827414215e-07,7.975549367259259e-08,1.2942451932425642e-08,1.909324866308246e-09,2.581989880118588e-10,3.223050695284231e-11,3.735898375918924e-12,4.0416597384708605e-13],[9.154315119468873e-05,0.00014855313151765712,0.00012053350029850566,6.519923004779395e-05,2.6450776682193412e-05,8.584685267950521e-06,2.1285783630043425e-06,3.3938385693337e-07,6.884258144387231e-08,1.2412823802862907e-08,2.0143110902644835e-09,2.971596319772191e-10,4.0185050542419045e-11,5.016226286867827e-12,5.814401760968484e-13,6.290276430450307e-14],[1.2212063436244833e-05,1.9817323765578495e-05,1.607944158168098e-05,8.697724766374178e-06,3.528593439982356e-06,1.1452164329524502e-06,3.097364196744665e-07,6.582801354888642e-08,9.183756083723254e-09,1.6558987726029535e-09,2.687136557307913e-10,3.964176706872547e-11,5.360776639303617e-12,6.691759331673841e-13,7.756543468527714e-14,8.391371041707351e-15],[1.4254772748862992e-06,2.3132163392677922e-06,1.8769046432824736e-06,1.0152591380162862e-06,4.11882053124546e-07,1.3367765476511878e-07,3.615459662125406e-08,8.38149390557046e-09,1.55864769821456e-09,1.9328806161061467e-10,3.136613330708743e-11,4.6272637206493555e-12,6.257472633485138e-13,7.811088524154101e-14,9.053978882256715e-15,9.794993931648774e-16],[1.4790369443210174e-07,2.4001311604613144e-07,1.94742586029922e-07,1.0534056204476294e-07,4.273577587005633e-08,1.3870034514830935e-08,3.751303865165008e-09,8.696413021336277e-10,1.76403063805251e-10,2.9159503857825544e-11,3.25446576939507e-12,4.80112458790521e-13,6.49258558242569e-14,8.104575713777929e-15,9.39416537596372e-16,1.0163022693900363e-16],[1.3811481172555601e-08,2.241280480630142e-08,1.8185371033323394e-08,9.836868476977598e-09,3.990734417352928e-09,1.2952057844114644e-09,3.503026946365191e-10,8.12084817584408e-11,1.647279740970786e-11,2.9701665378958625e-12,4.418728488990255e-13,4.483366159821508e-14,6.062879218615073e-15,7.568181127063184e-16,8.772420372606708e-17,9.490391509963149e-18],[1.1724890732710085e-09,1.9026756369159124e-09,1.5437988557171856e-09,8.350748670879984e-10,3.3878281700666135e-10,1.0995306085472157e-10,2.973801844040098e-11,6.8939787361764615e-12,1.3984144587959242e-12,2.5214441289599207e-13,4.0917143053902185e-14,5.5338723020026486e-15,5.146920556582633e-16,6.424806698972986e-17,7.447113676308309e-18,8.056616236502308e-19],[9.124073845646843e-11,1.4806238634789655e-10,1.2013531796157667e-10,6.498384443531188e-11,2.6363396559266427e-11,8.556325765958735e-12,2.314152706911501e-12,5.364755417610121e-13,1.0882179697656862e-13,1.9621370428742105e-14,3.184089671174341e-15,4.697302812071574e-16,5.823496621118441e-17,4.9996551867129054e-18,5.795193888673288e-19,6.269496506505485e-20],[6.554003557726674e-12,1.0635615442246782e-11,8.629558623141317e-12,4.667918682256091e-12,1.8937351644257964e-12,6.146178829746893e-13,1.6623018764208107e-13,3.8536104253612054e-14,7.816885928459707e-15,1.409442029656565e-15,2.287194885314733e-16,3.374165955125943e-17,4.562902051771297e-18,5.2217287718712115e-19,4.1628029328370613e-20,4.503503928609298e-21],[4.371594497447007e-13,7.09407578661974e-13,5.756013200182979e-13,3.1135545542729204e-13,1.2631427724304211e-13,4.09957079147001e-14,1.1087741518678172e-14,2.5704017372637537e-15,5.213951321667944e-16,9.401137742827784e-17,1.525584856212525e-17,2.250606853197675e-18,3.0435072740228937e-19,3.799154408456306e-20,4.037155012914185e-21,3.0038880540931843e-22],[2.721509440196574e-14,4.416373530077077e-14,3.5833708436000625e-14,1.938324361275804e-14,7.86361814091641e-15,2.5521627443385768e-15,6.902605726849654e-16,1.6001878941759692e-16,3.24591353359318e-17,5.8526208527885716e-18,9.497435296041317e-19,1.4011015433214541e-19,1.8947168550050662e-20,2.365140360894968e-21,2.7414784527019662e-22,2.719005547634791e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.20563397846079917, "-10": 2.508312140122776e-06, "-11": 3.658765052672231e-07, "-12": 4.900532023536748e-08, "-13": 6.066154594617175e-09, "-14": 6.951316194211326e-10, "-15": 6.830222108641841e-11, "-2": 0.13295389876679306, "-3": 0.06434021063086079, "-4": 0.024343623489486217, "-5": 0.007533203917392664, "-6": 0.0019682572397939626, "-7": 0.0004445044025891764, "-8": 8.833701332201248e-05, "-9": 1.56675575269187e-05, "0": 0.2774212336622487, "1": 0.19086797955714618, "10": 1.5839088912555332e-08, "11": 1.3295002373156147e-09, "12": 1.0247133846234628e-10, "13": 7.29924484482465e-12, "14": 4.813231850454714e-13, "15": 2.721509440196574e-14, "2": 0.06982443828105903, "3": 0.01944438144440678, "4": 0.004233525271642226, "5": 0.0007538795075230732, "6": 0.00011334682320628872, "7": 1.4730206737995344e-05, "8": 1.6845378260950446e-06, "9": 1.7192721735968857e-07} |
| Raw goal margin distribution | {"-1": 0.2558630820685282, "-10": 2.7304414569180577e-06, "-11": 3.9186346622932294e-07, "-12": 5.163794473904136e-08, "-13": 6.2885678189230995e-09, "-14": 7.091057383241717e-10, "-15": 6.87342027403923e-11, "-2": 0.1635828772711812, "-3": 0.07811120290520517, "-4": 0.02912874535849254, "-5": 0.008878638049007091, "-6": 0.002284070011228243, "-7": 0.0005077546386058719, "-8": 9.931040178474355e-05, "-9": 1.733297364515286e-05, "0": 0.23886848371256073, "1": 0.14975312911929933, "10": 1.0871404954372837e-08, "11": 8.978274102908073e-10, "12": 6.808200124706985e-11, "13": 4.771120596702995e-12, "14": 3.0958857517063547e-13, "15": 1.7268400222062104e-14, "2": 0.05416869881756246, "3": 0.014884325783152786, "4": 0.0031940587535814213, "5": 0.0005602382460340488, "6": 8.293561971220778e-05, "7": 1.0609400945927072e-05, "8": 1.1940897822425364e-06, "9": 1.1992800251341994e-07} |
| Research history json | {"away": [{"away": "Rio Ave", "away_goals": 1.0, "away_xg": 1.08, "date": "2026-11-01T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 2.0, "home_xg": 0.86, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 0.77, "date": "2026-10-25T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 1.0, "home_xg": 2.22, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 1.0, "away_xg": 1.36, "date": "2026-10-10T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 2.0, "home_xg": 0.73, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 2.54, "date": "2026-09-20T00:00:00+00:00", "home": "Estrela", "home_goals": 0.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Guimaraes", "away_goals": 1.0, "away_xg": 2.1, "date": "2026-09-12T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 2.0, "home_xg": 1.83, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 1.0, "away_xg": 0.33, "date": "2026-09-06T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": 1.88, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 3.0, "away_xg": 1.47, "date": "2026-08-29T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 0.0, "home_xg": 0.8, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 1.84, "date": "2026-08-22T00:00:00+00:00", "home": "Maritimo", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 1.26, "date": "2026-08-15T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 0.0, "home_xg": 0.69, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 1.18, "date": "2026-08-09T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": 3.12, "source": "pipeline training history"}], "h2h": [], "home": [{"away": "Nacional", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-11-01T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 0.0, "away_xg": 1.67, "date": "2026-10-25T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.21, "date": "2026-10-11T00:00:00+00:00", "home": "Rio Ave", "home_goals": 3.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.45, "date": "2026-09-19T00:00:00+00:00", "home": "Nacional", "home_goals": 0.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 3.0, "away_xg": 1.16, "date": "2026-09-12T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 2.2, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.08, "date": "2026-09-05T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 2.0, "home_xg": 3.0, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 3.0, "away_xg": 2.1, "date": "2026-08-30T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.42, "date": "2026-08-23T00:00:00+00:00", "home": "Guimaraes", "home_goals": 1.0, "home_xg": 3.14, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-08-16T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 2.08, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.24, "date": "2026-08-10T00:00:00+00:00", "home": "Santa Clara", "home_goals": 2.0, "home_xg": 1.44, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 22.3% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 53.8% |
| Raw p over 1 5 | 71.0% |
| Raw p under 3 5 | 75.4% |
| Raw p btts yes | 47.3% |
| P home draw | 56.3% |
| P draw away | 71.5% |
| P home away | 72.3% |
| Raw p home draw | 46.2% |
| Raw p draw away | 77.7% |
| Raw p home away | 76.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0167 |
| Totals anchor target over 2 5 | 0.4519 |
| Totals anchor reference over odds | 2.11 |
| Totals anchor reference under odds | 1.76 |
| Totals anchor reference last update utc | 2026-11-06T12:16:29Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4422 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.56, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.06, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.85, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.56, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.44, "draw": 3.23, "home": 3.05}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.11, "under": 1.76}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.34, "under": 3.31}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.05 |
| Reference draw odds | 3.23 |
| Reference away odds | 2.44 |
| Market reference 1x2 last update utc | 2026-11-06T12:16:29Z |
| Market reference home last update utc | 2026-11-06T12:16:29Z |
| Market reference draw last update utc | 2026-11-06T12:16:29Z |
| Market reference away last update utc | 2026-11-06T12:16:29Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-11-06T12:16:21Z |
| Market reference under 2 5 last update utc | 2026-11-06T12:16:21Z |
| Home probability edge | -2.7% |
| Draw probability edge | -1.7% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.0894 |
| Raw ev home | -0.3209 |
| Raw edge prob draw | -0.0551 |
| Raw ev draw | -0.2285 |
| Raw edge prob away | 0.1445 |
| Raw ev away | 0.3139 |
| Market p home draw | 60.8% |
| Market reference home draw last update utc | 2026-11-06T12:16:22Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.3% |
| Market reference draw away last update utc | 2026-11-06T12:16:22Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.8% |
| Market reference home away last update utc | 2026-11-06T12:16:22Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home draw odds | 1.55 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 72.8% |
| Market over 1 5 odds | 1.34 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T12:16:29Z |
| Market reference over 1 5 odds | 1.34 |
| Market reference over 1 5 opposite odds | 3.31 |
| Market reference over 1 5 last update utc | 2026-11-06T12:16:29Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.2% |
| Market under 3 5 odds | 1.28 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T12:16:29Z |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 3.70 |
| Market reference under 3 5 last update utc | 2026-11-06T12:16:29Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,377.6402 |
| Elo away rating | 1,452.3265 |
| Elo rating diff | -14.6862 |
| Elo home expectancy | 0.4789 |
| Research p home | 0.2805 |
| Research p draw | 0.2544 |
| Research p away | 0.4651 |
| Research p over 1 5 | 0.7438 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [0.9184429524432026, 1.596051518098783], "coverage": {"form": "last ten, exponential rank half-life five matches", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:18.180744+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T12:17:18.065934+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:18.182124+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Nacional%22+%22Acad%C3%A9mico+de+Viseu%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:18.264703+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Nacional_vs_Acad%C3%A9mico+de+Viseu&d=2026-11-07"}]}, "form": {"away": {"all": {"goals_against": 1.0650527153129232, "goals_for": 1.649570964958943, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 2.3738678769859316, "results": "WWWWWWLDLD", "xg_against": 1.584486958053463, "xg_for": 1.1369674333411801, "xg_matches": 10}, "venue": {"goals_against": 0.8979146949535403, "goals_for": 1.8037913442624962, "last_match": "2026-10-25T00:00:00+00:00", "matches": 5, "points_per_game": 2.3609841784542116, "results": "WWWDD", "xg_against": 1.8155259012043192, "xg_for": 1.326331413049327, "xg_matches": 5}}, "home": {"all": {"goals_against": 1.8804243500740794, "goals_for": 0.874261798272425, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.6711447942719047, "results": "LWLLLLLLWD", "xg_against": 1.6090907760595652, "xg_for": 0.9211553615670336, "xg_matches": 10}, "venue": {"goals_against": 2.00259287486749, "goals_for": 1.0941233506910442, "last_match": "2026-10-25T00:00:00+00:00", "matches": 5, "points_per_game": 1.2227916852143603, "results": "WLLLW", "xg_against": 1.4674034895920058, "xg_for": 1.2859261160044595, "xg_matches": 5}}}, "goal_rates": [1.1292039711635982, 1.5296568291727441], "h2h": [], "margin_distribution": {"-1": 0.23044886547383236, "-10": 1.5819953383861484e-06, "-11": 2.1718067307299536e-07, "-12": 2.73837445977847e-08, "-13": 3.1913676572393474e-09, "-14": 3.4396452958428295e-10, "-15": 3.145444050113332e-11, "-2": 0.14054469871736228, "-3": 0.06324657478740582, "-4": 0.022356841172642264, "-5": 0.006480840079963479, "-6": 0.0015888133804528625, "-7": 0.0003370347732510822, "-8": 6.296101213629434e-05, "-9": 1.0502482971677116e-05, "0": 0.25440509921557203, "1": 0.1701190548627363, "10": 7.603071380270666e-08, "11": 7.705191377033716e-09, "12": 7.171887650785433e-10, "13": 6.170152076463631e-11, "14": 4.909203951884561e-12, "15": 3.3140401610320145e-13, "2": 0.07658985415644907, "3": 0.025443225739559996, "4": 0.006639325927185609, "5": 0.001420768236465117, "6": 0.0002571243516851761, "7": 4.026460277483097e-05, "8": 5.5526307730707575e-06, "9": 6.83750201922948e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:18.265080+00:00", "p_over_1_5": 0.7437774709803133, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Sporting Lisbon vs Moreirense FC

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **84.0%**. Expected goals are 2.87 for Sporting Lisbon and 0.69 for Moreirense FC (3.56 combined). The most likely exact score is 2-0 at 12.8%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 67.5%; Under 3.5 goals: 54.6%; Double Chance 1X: 94.2%; Double Chance X2: 16.0%; Double Chance 12 (either team wins): 89.7%; Under 4.5 goals: 73.4%; BTTS Yes (both teams score): 44.5%; BTTS No (at least one team does not score): 55.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 84.0% | 1.19 |
| Draw | 10.3% | 9.75 |
| Moreirense FC win | 5.8% | 17.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Lisbon expected goals | 2.87 |
| Moreirense FC expected goals | 0.69 |
| Expected total goals | 3.56 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 85.8% |
| Under 1.5 | 14.2% |
| Over 2.5 | 67.5% |
| Under 2.5 | 32.5% |
| Over 3.5 | 45.4% |
| Under 3.5 | 54.6% |
| Over 4.5 | 26.6% |
| Under 4.5 | 73.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.81% |
| 2 | 3-0 | 11.79% |
| 3 | 1-0 | 9.58% |
| 4 | 2-1 | 8.51% |
| 5 | 4-0 | 8.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 84.0% | 84.8% | 1.16 | -2.6% |
| Draw | 10.3% | 9.8% | 8.06 | -17.3% |
| Moreirense FC win | 5.8% | 5.5% | 13.55 | -21.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T20:30:00+00:00 |
| Fixture id | ba0a2d492dfcc89ab465eddd7a9e98c2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T12:16:29Z |
| Market best draw last update utc | 2026-11-06T12:16:29Z |
| Market best away last update utc | 2026-11-06T12:16:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sp Lisbon |
| Matched away-team name | Moreirense |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8699 |
| Dc lambda away | 0.6904 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 44.5% |
| P btts no | 55.5% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.55 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 7.03 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.08 |
| Fair Over 3.5 odds | 2.20 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.75 |
| Fair Under 4.5 odds | 1.36 |
| Score matrix json | [[0.025285472972084444,0.021192814853944215,0.006185099733843737,0.0013695740124478836,0.0002274498055353409,3.02186890626522e-05,3.3456801839419745e-06,3.175019804091936e-07,2.6364315854709837e-08,1.9459606368189803e-09,1.2926891556092475e-10,7.806591867614285e-12,4.321557374882942e-13,2.2082944726847697e-14,1.0478255987665674e-15,4.6404254463217795e-17,1.926628016766817e-18,7.528509530867575e-20,2.7784114106582538e-21,9.714109785927062e-23],[0.09581925185056153,0.04851669968913536,0.017080513561891136,0.0037821584938440623,0.0006281159003529245,8.345067186757229e-05,9.239290911168206e-06,8.768002321178962e-07,7.280659550925358e-08,5.373883765563326e-09,3.569836478606279e-10,2.1558358636857456e-11,1.1934232676359239e-12,6.098333949726152e-14,2.8936314886399898e-15,1.281480544851088e-16,5.320495608023843e-18,2.0790418049232878e-19,7.672745116879365e-21,2.6826080593710047e-22],[0.12805201886030182,0.08506413387948765,0.02342188941149692,0.0052223256072848135,0.0008672893418123046,0.00011522694814309743,1.2757420292428635e-05,1.210667483162155e-06,1.0052982938870962e-07,7.420146682152919e-09,4.929155794604746e-10,2.9767332210835765e-11,1.6478539704374339e-12,8.420452394912855e-14,3.995466040295809e-15,1.7694416232174572e-16,7.346429427125664e-18,2.870697585555539e-19,1.0594366515117461e-20,3.7040892880517736e-22],[0.11787437222194917,0.07830318857047663,0.026008152682920102,0.004774123931790829,0.0007983566960583563,0.00010606864535448124,1.1743453336585965e-05,1.1144429491810816e-06,9.253966188304632e-08,6.8303892413265826e-09,4.537383713622521e-10,2.7401407867707252e-11,1.5168816080179455e-12,7.751190092192051e-14,3.677904147280817e-15,1.6288054056194585e-16,6.762531075281248e-18,2.642532923323774e-19,9.752320292748304e-21,3.40968618354605e-22],[0.08137923800645025,0.05405970525418591,0.017955757535710874,0.003975964811070605,0.0005473788062124443,7.322868722533721e-05,8.107557784453824e-06,7.693997965499228e-07,6.388841804592502e-08,4.715629540745151e-09,3.1325624238507806e-10,1.8917646393731886e-11,1.0472392520917563e-12,5.3513408509019267e-14,2.5391866893925483e-15,1.1245102754016327e-16,4.668780970176422e-18,1.8243771877921616e-19,6.73290028407818e-21,2.354011802799917e-22],[0.04494670217910048,0.02985780564518505,0.009917174283369027,0.0021959717320480373,0.00036469248019879345,4.0166338271413086e-05,4.477898713045337e-06,4.249484802186138e-07,3.528631834051401e-08,2.604497188067073e-09,1.7301507579992612e-10,1.0448436717006446e-11,5.784024516216442e-13,2.955607958202787e-14,1.4024224200307334e-15,6.21080138914662e-17,2.5786221762034523e-18,1.0076247963336759e-19,3.7186593446114195e-21,1.3001481706937219e-22],[0.020687156477354335,0.013742345211248555,0.004564475840646764,0.001010717330488555,0.00016785325815282923,2.230076831384808e-05,2.046793422863569e-06,1.955866677396421e-07,1.6240870934450398e-08,1.1987451417386986e-09,7.963187002579825e-11,4.808994538623846e-12,2.662153493687484e-13,1.3603472858457098e-14,6.454785477902294e-16,2.8585816969412446e-17,1.1868359160708585e-18,4.637691047756022e-20,1.7115491018988017e-21,5.984058306149412e-23],[0.008161255551327256,0.005421469657578635,0.0018007237405564234,0.0003987364060064048,6.621950853456972e-05,8.79783886197644e-06,9.740579772008741e-07,7.66288317897941e-08,6.407158867738404e-09,4.729149437889642e-10,3.141543604709714e-11,1.8971884037136478e-12,1.0502417286119363e-13,5.3666833576158605e-15,2.5464666384586535e-16,1.1277342910139686e-17,4.682166550608801e-19,1.8296077496330753e-20,6.752203776546858e-22,2.3607608481131207e-23],[0.002817222884938736,0.0018714630724738902,0.000621600450989801,0.0001376417293876775,2.2858629251310048e-05,3.0369681262992132e-06,3.3623973754640724e-07,3.190884265496888e-08,2.196476205154649e-09,1.6324777405789166e-10,1.0844444805777219e-11,6.548995499979484e-13,3.625379715112565e-14,1.852551127238804e-15,8.790270129982684e-17,3.8928800020948094e-18,1.6162594927351077e-19,6.315710603976007e-21,2.3308255553845467e-22,8.149223419538742e-24],[0.0008644361406847286,0.0005742393775274527,0.00019073176558879028,4.223396238371931e-05,7.013937504548992e-06,9.318627292556987e-07,1.0317173789243271e-07,9.790903284877079e-09,8.130042728323751e-10,4.974572400299961e-11,3.3275074066347676e-12,2.0094925487186044e-13,1.1124108306101444e-14,5.684364398048969e-16,2.6972048350742124e-17,1.1944905684069706e-18,4.9593275907077424e-20,1.9379114550609514e-21,7.151900754738377e-23,2.5005061828882838e-24],[0.0002387190806894005,0.00015857955243567576,5.267168920489192e-05,1.1663154974207925e-05,1.9369397394382018e-06,2.5733932628086156e-07,2.8491477002917062e-08,2.703815031881139e-09,2.245158704879769e-10,1.6571605677858e-11,9.125780698775114e-13,5.54933084475537e-14,3.0719873722752773e-15,1.5697703734725166e-16,7.448488423331107e-18,3.298655354187333e-19,1.3695472315092746e-20,5.351655480798913e-22,1.9750390954276956e-23,6.905293626021094e-25],[5.993060552644045e-05,3.9811516423973675e-05,1.3223267361090376e-05,2.9280438661811277e-06,4.86270184676995e-07,6.460523224720615e-08,7.152806822966659e-09,6.787948061133909e-10,5.6364878876805166e-11,4.160314122990529e-12,2.7636699576354966e-13,1.3835629695016586e-14,7.712247502728028e-16,3.94092038005455e-17,1.8699486449837664e-18,8.281299183482466e-20,3.4382586697459304e-21,1.3435371508927458e-22,4.958350567769702e-24,1.733579180810279e-25],[1.379182180449892e-05,9.161818664489954e-06,3.043068654411392e-06,6.738303223101895e-07,1.1190528907549696e-07,1.4867592993009699e-08,1.6460744262101148e-09,1.5621095307647096e-10,1.2971241633093403e-11,9.574125028606823e-13,6.360029778998252e-14,3.840842675524123e-15,1.7625875969562093e-16,9.069234517153516e-18,4.3033101816069875e-19,1.905774214110736e-20,7.9124598315611e-22,3.091880152063849e-23,1.1410645174400164e-24,3.9894833258736564e-26],[2.9297630846339417e-06,1.9462228044867143e-06,6.464316559537431e-07,1.4314013272469976e-07,2.3771767758899964e-08,3.1582865357260634e-09,3.4967157760820597e-10,3.318351195558802e-11,2.7554492392083686e-12,2.0338080403077865e-13,1.3510456216598882e-14,8.159008464687795e-16,4.516647443627576e-17,1.9132788785032078e-18,9.14141691396338e-20,4.048389704634639e-21,1.6808245532576926e-22,6.568005634088276e-24,2.4239355378641084e-25,8.474762174707444e-27],[5.779079706946812e-07,3.839005540617488e-07,1.275113364778117e-07,2.823498734821223e-08,4.6890801981306295e-09,6.229851732061921e-10,6.897417503996391e-11,6.545585940158923e-12,5.435238386799706e-13,4.0117710661360636e-14,2.6649937587938254e-15,1.609398401337828e-16,8.909275197643716e-18,4.552595619563433e-19,1.7907562594014624e-20,7.98561730488513e-22,3.315496436423677e-23,1.2955664665907418e-24,4.7813138035930704e-26,1.6716821357304922e-27],[1.0639510388666667e-07,7.067758432618653e-08,2.347533271599735e-08,5.198170927700977e-09,8.632778921760103e-10,1.1469399209609463e-10,1.2698413745795447e-11,1.2050678160143311e-12,1.000648515225048e-13,7.385826480953197e-15,4.906357105325126e-16,2.9629650184534036e-17,1.640232196605227e-18,8.381505507099818e-20,3.976985920661595e-21,1.460051691613944e-22,6.103957821608515e-24,2.3851882271031686e-25,8.802584574781675e-27,3.0776317946044812e-28],[1.8363517698340267e-08,1.2198766890931274e-08,4.051781257376706e-09,8.971907573069934e-10,1.489995147563055e-10,1.9795884178969978e-11,2.191713124413658e-12,2.0799156501272645e-13,1.7270932634951698e-14,1.2747744054494148e-15,8.468244519408421e-17,5.1140004162119e-18,2.83099803199894e-19,1.4466260109329355e-20,6.864174071197223e-22,3.039884506110624e-23,1.0462670263991108e-24,4.116772729404788e-26,1.519303160813941e-27,5.311912283989664e-29],[2.9830544048251254e-09,1.9816238862947485e-09,6.581900116173214e-10,1.4574379944616564e-10,2.420416752999213e-11,3.215734614007079e-12,3.560319758608188e-13,3.378710791526411e-14,2.8055698542326217e-15,2.070802265558252e-16,1.3756206479459367e-17,8.307417847963433e-19,4.5988036105789123e-20,2.3499659296966428e-21,1.1150480553310313e-22,4.938128421295091e-24,2.0502293759294875e-25,6.641389754126317e-27,2.468026039771448e-28,8.628915002615335e-30],[4.576599265442372e-10,3.0402055047102835e-10,1.0097944974845094e-10,2.2360000019081248e-11,3.713401108582862e-12,4.933577023777133e-13,5.4622392289025e-14,5.183614922218783e-15,4.3043026346618025e-16,3.1770228903974264e-17,2.1104759057472844e-18,1.2745232657914303e-19,7.055480178988892e-21,3.605315521657318e-22,1.7107056789532815e-23,7.576071984809838e-25,3.145459982456245e-26,1.229122863925969e-27,3.7603496560739637e-29,1.3238473290549684e-30],[6.651866172827701e-11,4.418791985553525e-11,1.4676875709972154e-11,3.24991809692511e-12,5.39724930841976e-13,7.17071611738131e-14,7.939101120123299e-15,7.534134136329966e-16,6.256096160595889e-17,4.617649453057632e-18,3.0674748807510684e-19,1.852458060336735e-20,1.025479995376788e-21,5.2401521238641533e-23,2.4864281483892716e-24,1.1011455020585688e-25,4.571774289541491e-27,1.786470767177378e-28,6.59300588513838e-30,1.9108882933190965e-31]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.04437191946557506, "-10": 1.5255524256921244e-10, "-11": 9.088012640056615e-12, "-12": 4.9730219484502e-13, "-13": 2.5160469125103426e-14, "-14": 1.1835911988862356e-15, "-15": 5.202180755127022e-17, "-16": 2.145467532392618e-18, "-17": 8.33282493543603e-20, "-18": 3.0466722165953544e-21, "-19": 9.714109785927062e-23, "-2": 0.01094916544595364, "-3": 0.002125466231222142, "-4": 0.00032483891512564506, "-5": 4.076608067938072e-05, "-6": 4.330164611040152e-06, "-7": 3.982019708828702e-07, "-8": 3.2259594059852495e-08, "-9": 2.334283443389812e-09, "0": 0.10258785681839458, "1": 0.21125550326922848, "10": 0.00028172161190063576, "11": 6.976797426928687e-05, "12": 1.5870906387016324e-05, "13": 3.3380608676333285e-06, "14": 6.527868651859603e-07, "15": 1.192749605141652e-07, "16": 2.044937095248039e-08, "17": 3.3017518310061256e-09, "18": 5.018478463997725e-10, "19": 6.651866172827701e-11, "2": 0.22668393405493362, "3": 0.18293133149954244, "4": 0.11622407557371814, "5": 0.060634691448937815, "6": 0.02677446377308711, "7": 0.01023561503846033, "8": 0.0034471771293095956, "9": 0.00103693719846598} |
| Raw goal margin distribution | {"-1": 0.049481056951774065, "-10": 2.303635933303845e-10, "-11": 1.4246361307616061e-11, "-12": 8.094183993437833e-13, "-13": 4.252497819451596e-14, "-14": 2.0775146959028833e-15, "-15": 9.483771223029886e-17, "-16": 4.062564915840342e-18, "-17": 1.6389450949902558e-19, "-18": 6.220900782374692e-21, "-19": 2.0468923484836186e-22, "-2": 0.01251676101533908, "-3": 0.002502399025698183, "-4": 0.0003950745682625752, "-5": 5.1307753766544693e-05, "-6": 5.645971439089297e-06, "-7": 5.38274320665142e-07, "-8": 4.523181294733108e-08, "-9": 3.3961044053773457e-09, "0": 0.11399578237400525, "1": 0.19680738928439362, "10": 0.00035510392719297496, "11": 9.129347714764878e-05, "12": 2.156269448802023e-05, "13": 4.709428633031922e-06, "14": 9.564502566778187e-07, "15": 1.815070571846876e-07, "16": 3.232264730300168e-08, "17": 5.4208223841115535e-09, "18": 8.553585693617375e-10, "19": 1.169995258017736e-10, "2": 0.21631183746967134, "3": 0.17977903776053786, "4": 0.1179928596157606, "5": 0.06370210995281071, "6": 0.02914094662957916, "7": 0.01154948989598592, "8": 0.004034570418965453, "9": 0.0012592979637050777} |
| Research history json | {"away": [{"away": "Estrela", "away_goals": 1.0, "away_xg": 0.68, "date": "2026-10-31T00:00:00+00:00", "home": "Moreirense", "home_goals": 2.0, "home_xg": 0.44, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 3.0, "away_xg": 1.33, "date": "2026-10-25T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 2.01, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": 1.49, "date": "2026-10-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 0.0, "home_xg": 1.09, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.52, "date": "2026-09-20T00:00:00+00:00", "home": "Guimaraes", "home_goals": 1.0, "home_xg": 1.07, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.76, "date": "2026-09-14T00:00:00+00:00", "home": "Moreirense", "home_goals": 3.0, "home_xg": 1.99, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 4.0, "away_xg": 2.99, "date": "2026-09-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 0.0, "home_xg": 0.38, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.85, "date": "2026-09-04T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.9, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.28, "date": "2026-08-30T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.78, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 0.0, "away_xg": 0.49, "date": "2026-08-16T00:00:00+00:00", "home": "Arouca", "home_goals": 4.0, "home_xg": 2.14, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 2.0, "away_xg": 1.5, "date": "2026-08-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 2.0, "home_xg": 0.2, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 82.1% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 6.5% |
| Raw p over 1 5 | 86.8% |
| Raw p under 3 5 | 52.4% |
| Raw p btts yes | 46.8% |
| P home draw | 94.2% |
| P draw away | 16.0% |
| P home away | 89.7% |
| Raw p home draw | 93.5% |
| Raw p draw away | 17.9% |
| Raw p home away | 88.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9622 |
| Totals anchor target over 2 5 | 0.6749 |
| Totals anchor reference over odds | 1.43 |
| Totals anchor reference under odds | 2.78 |
| Totals anchor reference last update utc | 2026-11-06T12:16:29Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6967 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 4.31, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.31, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 13.55, "draw": 8.06, "home": 1.16}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.43, "under": 2.78}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.13, "under": 5.65}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.16 |
| Reference draw odds | 8.06 |
| Reference away odds | 13.55 |
| Market reference 1x2 last update utc | 2026-11-06T12:16:29Z |
| Market reference home last update utc | 2026-11-06T12:16:29Z |
| Market reference draw last update utc | 2026-11-06T12:16:29Z |
| Market reference away last update utc | 2026-11-06T12:16:29Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-11-06T12:16:22Z |
| Market reference under 2 5 last update utc | 2026-11-06T12:16:22Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | -0.0265 |
| Raw ev home | -0.0476 |
| Raw edge prob draw | 0.0163 |
| Raw ev draw | -0.0812 |
| Raw edge prob away | 0.0102 |
| Raw ev away | -0.1199 |
| Market p home draw | 92.6% |
| Market reference home draw last update utc | 2026-11-06T12:16:22Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 19.1% |
| Market reference draw away last update utc | 2026-11-06T12:16:22Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 88.3% |
| Market reference home away last update utc | 2026-11-06T12:16:22Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 5.00 |
| Market reference dc home draw odds | 1.03 |
| Market reference dc home away odds | 1.08 |
| Market p over 1 5 | 86.7% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T12:16:29Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 5.65 |
| Market reference over 1 5 last update utc | 2026-11-06T12:16:29Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 55.7% |
| Market under 3 5 odds | 1.72 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T12:16:29Z |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 2.13 |
| Market reference under 3 5 last update utc | 2026-11-06T12:16:29Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,667.4354 |
| Elo away rating | 1,438.9672 |
| Elo rating diff | 288.4681 |
| Elo home expectancy | 0.8403 |
| Research p home | 0.8182 |
| Research p draw | 0.1196 |
| Research p away | 0.0621 |
| Research p over 1 5 | 0.8703 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.8699040188461877, 0.6903561678381339], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:18.180744+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T12:17:18.065934+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:18.388299+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Sporting+Lisbon%22+%22Moreirense+FC%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:18.471206+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Sporting+Lisbon_vs_Moreirense+FC&d=2026-11-07"}]}, "form": {"away": {"all": {"goals_against": 1.4889998489640717, "goals_for": 1.4469006738231538, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 1.6256113882270293, "results": "WWLDWLLWLD", "xg_against": 1.5345832438249536, "xg_for": 0.827627807906664, "xg_matches": 10}, "venue": {"goals_against": 1.4714941649527495, "goals_for": 1.3690993918184686, "last_match": "2026-10-25T00:00:00+00:00", "matches": 5, "points_per_game": 1.514509847632683, "results": "WDLWL", "xg_against": 1.781999249674747, "xg_for": 0.7490016998175378, "xg_matches": 5}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [2.8699040188461877, 0.6903561678381339], "h2h": [], "margin_distribution": {"-1": 0.04666456034161134, "-10": 2.303635933303845e-10, "-11": 1.4246361307616061e-11, "-12": 8.094183993437833e-13, "-13": 4.252497819451596e-14, "-14": 2.0775146959028833e-15, "-15": 9.483771223029886e-17, "-16": 4.062564915840342e-18, "-17": 1.6389450949902558e-19, "-18": 6.220900782374692e-21, "-19": 2.0468923484836186e-22, "-2": 0.01251676101533908, "-3": 0.002502399025698183, "-4": 0.0003950745682625752, "-5": 5.1307753766544693e-05, "-6": 5.645971439089297e-06, "-7": 5.38274320665142e-07, "-8": 4.523181294733108e-08, "-9": 3.3961044053773457e-09, "0": 0.11962877559433072, "1": 0.19399089267423086, "10": 0.00035510392719297496, "11": 9.129347714764878e-05, "12": 2.156269448802023e-05, "13": 4.709428633031922e-06, "14": 9.564502566778187e-07, "15": 1.815070571846876e-07, "16": 3.232264730300168e-08, "17": 5.4208223841115535e-09, "18": 8.553585693617375e-10, "19": 1.169995258017736e-10, "2": 0.21631183746967134, "3": 0.17977903776053786, "4": 0.1179928596157606, "5": 0.06370210995281071, "6": 0.02914094662957916, "7": 0.01154948989598592, "8": 0.004034570418965453, "9": 0.0012592979637050777}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:18.471604+00:00", "p_over_1_5": 0.8703452987106259, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — CF Estrela vs Benfica

The model's most likely 1X2 outcome is **Benfica win** at **79.1%**. Expected goals are 0.72 for CF Estrela and 2.58 for Benfica (3.30 combined). The most likely exact score is 0-2 at 12.5%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 64.5%; Under 3.5 goals: 57.7%; Double Chance 1X: 20.9%; Double Chance X2: 92.0%; Double Chance 12 (either team wins): 87.1%; Under 4.5 goals: 76.0%; BTTS Yes (both teams score): 46.8%; BTTS No (at least one team does not score): 53.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CF Estrela win | 8.0% | 12.55 |
| Draw | 12.9% | 7.73 |
| Benfica win | 79.1% | 1.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CF Estrela expected goals | 0.72 |
| Benfica expected goals | 2.58 |
| Expected total goals | 3.30 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 84.0% |
| Under 1.5 | 16.0% |
| Over 2.5 | 64.5% |
| Under 2.5 | 35.5% |
| Over 3.5 | 42.3% |
| Under 3.5 | 57.7% |
| Over 4.5 | 24.0% |
| Under 4.5 | 76.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.49% |
| 2 | 0-3 | 10.75% |
| 3 | 0-1 | 10.02% |
| 4 | 1-2 | 8.98% |
| 5 | 1-3 | 7.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CF Estrela win | 8.0% | 7.8% | 10.27 | -18.2% |
| Draw | 12.9% | 12.6% | 6.61 | -14.5% |
| Benfica win | 79.1% | 79.7% | 1.23 | -2.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T20:30:00+00:00 |
| Fixture id | c02a3d0a40d536e48bb60dffe0e3cd1e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T12:16:29Z |
| Market best draw last update utc | 2026-11-06T12:16:29Z |
| Market best away last update utc | 2026-11-06T12:16:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Estrela |
| Matched away-team name | Benfica |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7193 |
| Dc lambda away | 2.5826 |
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
| P btts yes | 46.8% |
| P btts no | 53.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.85 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.26 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.82 |
| Fair Over 3.5 odds | 2.37 |
| Fair Under 3.5 odds | 1.73 |
| Fair Over 4.5 odds | 4.16 |
| Fair Under 4.5 odds | 1.32 |
| Score matrix json | [[0.031400147079248965,0.10016467390306404,0.12485068458261564,0.10747833217877525,0.06939244221937337,0.03584209720827801,0.015427423736656263,0.0056917604482309096,0.001837417598616102,0.0005272500231653697,0.0001361657406696951,3.196880575455934e-05,6.88012631995954e-06,1.3667979065503353e-06,2.5213173625170994e-07,4.3409771587982015e-08,7.006784543475872e-09,1.0644397569592817e-09,1.5272137562457858e-10],[0.028145846877553015,0.061086756526745806,0.08980402512404086,0.07730824124465151,0.04991338770244012,0.025780912687431896,0.011096813393354948,0.00409403440599254,0.001321638697786132,0.0003792464133079086,9.794284778665607e-05,2.299488741103611e-05,4.948815771093123e-06,9.831259952612526e-07,1.8135619241986415e-07,3.122427587280387e-08,5.039919943447904e-09,7.656423751024387e-10,1.0985117381949404e-10],[0.008964909880140605,0.02315246164500486,0.029862048031787318,0.027803576977730057,0.017951135543393188,0.0092719945366852,0.00399092128371237,0.0014724018930435056,0.00047532168212643033,0.00013639434394278077,3.522472460906992e-05,8.270012510098469e-06,1.7798203403018374e-06,3.5357704234339725e-07,6.522397580325974e-08,1.1229676730790246e-08,1.812585564659257e-09,2.7535999229636446e-10,3.950750292868179e-11],[0.0021494608934994716,0.005551122271114662,0.007168066784107972,0.006163582311725761,0.00430403254023864,0.002223088678838232,0.0009568784676104193,0.00035302867858410305,0.00011396493453062183,3.270242671919928e-05,8.445613959735282e-06,1.9828496568143155e-06,4.267364948540587e-07,8.477497660516576e-08,1.563834853691399e-08,2.692470008309337e-09,4.345924096780352e-10,6.60213591646354e-11,9.47246918043592e-12],[0.0003865221899428966,0.0009982186432704937,0.0012889822184853025,0.0011096267474546807,0.0007155983613733062,0.0003997621483510025,0.0001720686158694579,6.348262411828245e-05,2.049349965132809e-05,5.880643667525794e-06,1.5187143962477411e-06,3.565616820465213e-07,7.673697391675154e-08,1.5244478142814166e-08,2.8121324476563573e-09,4.841676380875964e-10,7.814964693208826e-11,1.1872149153537355e-11,1.7033664314905512e-12],[5.560441830603216e-05,0.00014360201935493684,0.0001854307678332331,0.00015962899785429478,0.00010306306197341709,5.3172300278787206e-05,2.475349551227268e-05,9.132501259912347e-06,2.9481596576261794e-06,8.459792966766841e-07,2.1847964430923975e-07,5.129435110399816e-08,1.1039249254580985e-08,2.19304443979124e-09,4.0454854344727595e-10,6.965152474801936e-11,1.1242473967982383e-11,1.7079069841305202e-12,2.450433689176983e-13],[6.665963420299754e-06,1.7215283196251704e-05,2.2229793117723068e-05,1.913662786038716e-05,1.235539588450933e-05,6.3817223630688995e-06,2.743715443790409e-06,1.0948216200980017e-06,3.5343098684673425e-07,1.0141760704950891e-07,2.619175528516411e-08,6.149264366824079e-09,1.3234061961336113e-09,2.6290633838272305e-10,4.849804879736579e-11,8.349957256688571e-12,1.347769161288265e-12,2.0474713751754962e-13,2.937626511264469e-14],[6.849671766762239e-07,1.768972192482856e-06,2.284242752304005e-06,1.9664017232251066e-06,1.2695900205448214e-06,6.557597265012082e-07,2.8225700944283564e-07,1.0401575067947917e-07,3.631712476445198e-08,1.0421259101784421e-08,2.6913578036206335e-09,6.318732921864415e-10,1.3598781580483053e-10,2.7015181599091334e-11,4.983461424026772e-12,8.580075057213453e-13,1.3849125460358316e-13,2.103897964559008e-14,3.018585027668163e-15],[6.158637590676468e-08,1.5905081312583788e-07,2.053795241522853e-07,1.7680198385257158e-07,1.1415064971749694e-07,5.8960292399398495e-08,2.5378130336430028e-08,9.362952685076678e-09,3.019084396814395e-09,9.369902709479222e-10,2.4198381913376476e-10,5.681262901803793e-11,1.2226858494936223e-11,2.42897351260613e-12,4.480701251500231e-13,7.714467871963146e-14,1.2451946248290625e-14,1.891644670384769e-15,2.7140528561177713e-16],[4.922061249687762e-09,1.2711542650328716e-08,1.641419197712912e-08,1.4130238722052766e-08,9.123064660465893e-09,4.712181326088759e-09,2.0282523541825617e-09,7.482990501607659e-10,2.415663582996465e-10,6.923829339056568e-11,1.9339653643735984e-11,4.540537345563397e-12,9.77186033717091e-13,1.9412664289608562e-13,3.5810332523583824e-14,6.1655005373323544e-15,9.951753323607102e-16,1.5118264053034736e-16,2.1691054549021362e-17],[3.5403963831414553e-10,9.143303453655117e-10,1.180658731374054e-09,1.0163759353391725e-09,6.562142055653618e-10,3.389431556677531e-10,1.4589044984561314e-10,5.382450799175696e-11,1.737566068010581e-11,4.985974610779539e-12,1.2861821398978004e-12,3.2659695156721413e-13,7.02881521364205e-14,1.3963362695340153e-14,2.5758064622546424e-15,4.4347915833052407e-16,7.158210693751445e-17,1.087443748818385e-17,1.5602189240686679e-18],[2.3150697374926502e-11,5.97881785979196e-11,7.720342593066443e-11,6.646095281940333e-11,4.290993109842559e-11,2.2163536437703002e-11,9.539795234088444e-12,3.519591483611828e-12,1.1361966812812302e-12,3.2603351953151093e-13,8.420027258345235e-14,1.9745731362900187e-14,4.596151286622895e-15,9.130660782376076e-16,1.6843231505938048e-16,2.8999159064463635e-17,4.680763157089159e-18,7.1108086261266975e-19,1.0202291563098117e-19],[1.387674815752443e-12,3.5837602805822876e-12,4.6276467666940974e-12,3.9837327128764354e-12,2.5720620751342184e-12,1.3285034504369747e-12,5.718243981763312e-13,2.109676604746519e-13,6.810470953946691e-14,1.9542759201501003e-14,5.047044408696507e-15,1.1849381609699045e-15,2.5472223227729936e-16,5.4730049007528026e-17,1.0095993134959514e-17,1.7382371710037144e-18,2.8056939479626123e-19,4.262286310561983e-20,6.115350581364433e-21],[7.678019821125361e-14,1.9828984540266672e-13,2.5604819801084164e-13,2.20420363505303e-13,1.423124738582011e-13,7.350624014429203e-14,3.163910603234728e-14,1.1672863558185329e-14,3.768240972741685e-15,1.0813029883174963e-15,2.7925351507557254e-16,6.55627570916284e-17,1.4110006302343474e-17,2.7998596858975716e-18,5.586123962488454e-19,9.617685138680443e-20,1.5523935074650417e-20,2.3583276430696863e-21,3.3836301159206913e-22],[3.944809795478755e-15,1.0187727340013027e-14,1.3155233551869211e-14,1.1324748168613905e-14,7.31172429836685e-15,3.776600515567782e-15,1.6255526594655387e-15,5.997278931075664e-16,1.9360452626204655e-16,5.555513947045415e-17,1.4347475356354728e-17,3.36848057727132e-18,7.249433105473967e-19,1.4401639637768717e-19,2.6536052388828858e-20,4.9413702268010335e-21,7.975880835624288e-22,1.2116605848988375e-22,1.7384400583123898e-23],[1.8916452035862e-16,4.885296518039287e-16,6.30829767229107e-16,5.430529395747508e-16,3.506173660084345e-16,1.8109842100176457e-16,7.794973777896912e-17,2.8758608178118814e-17,9.283871529520267e-18,2.664022311907001e-18,6.880010532453514e-19,1.6152794324004265e-19,3.476303313383083e-20,6.905983800736282e-21,1.2739393862553433e-21,2.1908362474363736e-22,3.824655055454379e-23,5.8102470147617524e-24,8.336300020847117e-25],[8.50402592687707e-18,2.1962198921408485e-17,2.835940210030879e-17,2.4413332209736685e-17,1.5762253752957557e-17,8.141408677461465e-18,3.504286056438678e-18,1.292863741593691e-18,4.173630659658667e-19,1.1976302304093134e-19,3.092957803834057e-20,7.261603891809596e-21,1.5627969478977022e-21,3.104634271834697e-22,5.727085369627894e-23,9.860379794165411e-24,1.5897398921323762e-24,2.612037984788116e-25,3.7476431297534953e-26],[3.5981604772219467e-19,9.292482975874259e-19,1.1999220213154842e-18,1.0329588342003403e-18,6.669208087264458e-19,3.4447325518575063e-19,1.4827075666957664e-19,5.470269325888607e-20,1.765915698662552e-20,5.0673243454791476e-21,1.3086694023706696e-21,3.0724760659737885e-22,6.612390719643068e-23,1.3136098630459677e-23,2.423201952094544e-24,4.172050881645523e-25,6.734120121517013e-26,1.0218434124601433e-26,1.5856750094791092e-27],[1.4378477377775728e-20,3.713335108253219e-20,4.7949644680384796e-20,4.127768987443925e-20,2.6650578321189188e-20,1.3765369661225267e-20,5.924993434993183e-21,2.185954302220472e-21,7.056711084738067e-22,2.0249349335185262e-22,5.229525896938832e-23,1.2277809143873954e-23,2.6423532518151613e-24,5.24926829100526e-25,9.683268623103221e-26,1.6671779816497932e-26,2.6909970925258466e-27,4.088043914256558e-28,5.858621745204047e-29]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2225019562843429, "-10": 0.0001610281065506902, "-11": 3.7287332534410554e-05, "-12": 7.931248647962542e-06, "-13": 1.5598304853031902e-06, "-14": 2.8523632241476914e-07, "-15": 4.873452399290672e-08, "-16": 7.811934421506993e-09, "-17": 1.1742909307787758e-09, "-18": 1.5272137562457858e-10, "-2": 0.22251471526546943, "-3": 0.16768712783605572, "-4": 0.09953867118410191, "-5": 0.04853138284023634, "-6": 0.020031053611117466, "-7": 0.0071586069728188095, "-8": 0.0022539505655769124, "-9": 0.0006339052774740264, "0": 0.1292841554319833, "1": 0.05968573870505687, "10": 4.186833804246783e-10, "11": 2.7002189510919645e-11, "12": 1.599679060298555e-12, "13": 8.762384933688387e-14, "14": 4.462758458795514e-15, "15": 2.1236791899121842e-16, "16": 9.48122386914488e-18, "17": 3.9694939880472686e-19, "18": 1.4378477377775728e-20, "2": 0.015977680667342068, "3": 0.0033535775660094138, "4": 0.000554439416449067, "5": 7.529021800084397e-05, "6": 8.655124337092513e-06, "7": 8.614928283973179e-07, "8": 7.55476854643359e-08, "9": 5.9177249220316525e-09} |
| Raw goal margin distribution | {"-1": 0.2187950144344507, "-10": 0.00015834533540948353, "-11": 3.666611564377785e-05, "-12": 7.799111933184804e-06, "-13": 1.5338432939936506e-06, "-14": 2.8048420931731204e-07, "-15": 4.7922593843883604e-08, "-16": 7.681785513518557e-09, "-17": 1.154726931127061e-09, "-18": 1.501769968329046e-10, "-2": 0.21880756084755362, "-3": 0.16489341562676024, "-4": 0.09788033041237644, "-5": 0.04772283707691861, "-6": 0.019697330923153348, "-7": 0.007039342674124013, "-8": 0.0022163991488673546, "-9": 0.0006233442467254561, "0": 0.13749914027914975, "1": 0.06340542530878802, "10": 4.4477622932224253e-10, "11": 2.8684998248388914e-11, "12": 1.6993729721099813e-12, "13": 9.3084672401442e-14, "14": 4.740882902172189e-15, "15": 2.2560294163603275e-16, "16": 1.0072105077590848e-17, "17": 4.2168775997990623e-19, "18": 1.527456128063999e-20, "2": 0.016973428831416833, "3": 0.0035625765298741554, "4": 0.0005889927438383349, "5": 7.998239441292897e-05, "6": 9.194522034914468e-06, "7": 9.151820915701379e-07, "8": 8.025590755660557e-08, "9": 6.28652461513459e-09} |
| Research history json | {"away": [{"away": "Alverca", "away_goals": 0.0, "away_xg": 0.56, "date": "2026-11-02T00:00:00+00:00", "home": "Benfica", "home_goals": 1.0, "home_xg": 1.6, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 2.0, "away_xg": 1.81, "date": "2026-10-26T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": 1.56, "source": "pipeline training history"}, {"away": "Guimaraes", "away_goals": 0.0, "away_xg": 0.43, "date": "2026-10-11T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": 2.76, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 1.0, "away_xg": 0.84, "date": "2026-09-20T00:00:00+00:00", "home": "Porto", "home_goals": 3.0, "home_xg": 1.3, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": 1.1, "date": "2026-09-13T00:00:00+00:00", "home": "Benfica", "home_goals": 3.0, "home_xg": 2.91, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 4.0, "away_xg": 2.99, "date": "2026-09-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 0.0, "home_xg": 0.38, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 3.0, "away_xg": 1.31, "date": "2026-09-05T00:00:00+00:00", "home": "Maritimo", "home_goals": 0.0, "home_xg": 0.13, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 1.0, "away_xg": 0.36, "date": "2026-08-31T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": 2.03, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 7.0, "away_xg": 3.04, "date": "2026-08-17T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.12, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 1.18, "date": "2026-08-09T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": 3.12, "source": "pipeline training history"}], "h2h": [{"away": "Estrela", "away_goals": 0.0, "away_xg": null, "date": "2026-01-25T00:00:00+00:00", "home": "Benfica", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 1.0, "away_xg": null, "date": "2025-08-16T00:00:00+00:00", "home": "Estrela", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 3.0, "away_xg": null, "date": "2025-02-02T00:00:00+00:00", "home": "Estrela", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 0.0, "away_xg": null, "date": "2024-08-24T00:00:00+00:00", "home": "Benfica", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 4.0, "away_xg": null, "date": "2024-01-29T00:00:00+00:00", "home": "Estrela", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 0.0, "away_xg": null, "date": "2023-08-19T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Estrela", "away_goals": 1.0, "away_xg": 0.68, "date": "2026-10-31T00:00:00+00:00", "home": "Moreirense", "home_goals": 2.0, "home_xg": 0.44, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 2.0, "away_xg": 0.79, "date": "2026-10-24T00:00:00+00:00", "home": "Estrela", "home_goals": 0.0, "home_xg": 1.69, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 0.0, "away_xg": 1.45, "date": "2026-10-11T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.74, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 2.54, "date": "2026-09-20T00:00:00+00:00", "home": "Estrela", "home_goals": 0.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 3.0, "away_xg": 1.87, "date": "2026-09-14T00:00:00+00:00", "home": "Rio Ave", "home_goals": 3.0, "home_xg": 1.24, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 1.0, "away_xg": 0.61, "date": "2026-09-10T00:00:00+00:00", "home": "Estrela", "home_goals": 2.0, "home_xg": 0.57, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": 1.81, "date": "2026-09-05T00:00:00+00:00", "home": "Estrela", "home_goals": 2.0, "home_xg": 0.94, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 3.0, "away_xg": 2.1, "date": "2026-08-30T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 2.0, "away_xg": 1.29, "date": "2026-08-15T00:00:00+00:00", "home": "Alverca", "home_goals": 2.0, "home_xg": 1.75, "source": "pipeline training history"}, {"away": "Sp Lisbon", "away_goals": 2.0, "away_xg": 2.62, "date": "2026-08-08T00:00:00+00:00", "home": "Estrela", "home_goals": 2.0, "home_xg": 1.01, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 8.5% |
| Unadjusted draw probability | 13.7% |
| Unadjusted away-win probability | 77.8% |
| Raw p over 1 5 | 83.8% |
| Raw p under 3 5 | 58.0% |
| Raw p btts yes | 47.1% |
| P home draw | 20.9% |
| P draw away | 92.0% |
| P home away | 87.1% |
| Raw p home draw | 22.2% |
| Raw p draw away | 91.5% |
| Raw p home away | 86.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6454 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -1.75, "market_key": "spreads", "opposite_price": 1.93, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 1.75, "market_key": "spreads", "opposite_price": 1.91, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.23, "draw": 6.61, "home": 10.27}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.27 |
| Reference draw odds | 6.61 |
| Reference away odds | 1.23 |
| Market reference 1x2 last update utc | 2026-11-06T12:16:29Z |
| Market reference home last update utc | 2026-11-06T12:16:29Z |
| Market reference draw last update utc | 2026-11-06T12:16:29Z |
| Market reference away last update utc | 2026-11-06T12:16:29Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-11-06T12:16:25Z |
| Market reference under 2 5 last update utc | 2026-11-06T12:16:25Z |
| Home probability edge | +0.2% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | 0.0071 |
| Raw ev home | -0.1309 |
| Raw edge prob draw | 0.0117 |
| Raw ev draw | -0.0911 |
| Raw edge prob away | -0.0188 |
| Raw ev away | -0.0432 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,369.8605 |
| Elo away rating | 1,697.2970 |
| Elo rating diff | -267.4365 |
| Elo home expectancy | 0.1766 |
| Research p home | 0.1115 |
| Research p draw | 0.1735 |
| Research p away | 0.7150 |
| Research p over 1 5 | 0.8149 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [0.7192914113708055, 2.5825649063459117], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:18.484557+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T12:17:18.065934+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:18.784848+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22CF+Estrela%22+%22Benfica%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:18.867618+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=CF+Estrela_vs_Benfica&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 0.7555428435148334, "goals_for": 2.3450699791344993, "last_match": "2026-11-02T00:00:00+00:00", "matches": 10, "points_per_game": 2.5592486517835913, "results": "WWWLWWWWWD", "xg_against": 0.7758083739925704, "xg_for": 2.1102298851170693, "xg_matches": 10}, "venue": {"goals_against": 0.9350525536533023, "goals_for": 3.0813340821541915, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 2.323846319754449, "results": "WLWWW", "xg_against": 0.8114905046532553, "xg_for": 1.9203973892492832, "xg_matches": 5}}, "home": {"all": {"goals_against": 1.88202684170377, "goals_for": 1.2020655108450724, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 0.7358705894281937, "results": "LLLLDWDWDD", "xg_against": 1.1766693126000094, "xg_for": 1.2226669902694305, "xg_matches": 10}, "venue": {"goals_against": 1.8037913442624962, "goals_for": 1.0314331330207962, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 0.9081338779854057, "results": "LLWDD", "xg_against": 1.5954491586464379, "xg_for": 1.0494473812745448, "xg_matches": 5}}}, "goal_rates": [0.789683921901837, 2.307684362213228], "h2h": [{"away": "Estrela", "away_goals": 0.0, "away_xg": null, "date": "2026-01-25T00:00:00+00:00", "home": "Benfica", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 1.0, "away_xg": null, "date": "2025-08-16T00:00:00+00:00", "home": "Estrela", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 3.0, "away_xg": null, "date": "2025-02-02T00:00:00+00:00", "home": "Estrela", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 0.0, "away_xg": null, "date": "2024-08-24T00:00:00+00:00", "home": "Benfica", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 4.0, "away_xg": null, "date": "2024-01-29T00:00:00+00:00", "home": "Estrela", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 0.0, "away_xg": null, "date": "2023-08-19T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.23285861378134606, "-10": 6.28479508785416e-05, "-11": 1.300731871799218e-05, "-12": 2.4727963774776835e-06, "-13": 4.3464158057594354e-07, "-14": 7.103217288580597e-08, "-15": 1.0846130330660935e-08, "-16": 1.553749344844686e-09, "-17": 2.0875788810273892e-10, "-18": 2.4303249958586687e-11, "-2": 0.2121511378816433, "-3": 0.14317362014194535, "-4": 0.07605195094353213, "-5": 0.03316734681113504, "-6": 0.012241814204902984, "-7": 0.003911542652789599, "-8": 0.0011010033408724684, "-9": 0.0002767931306825172, "0": 0.17350334514363874, "1": 0.07968364581849505, "10": 1.3837575679432327e-09, "11": 9.80016882716832e-11, "12": 6.375452581629898e-12, "13": 3.83469497311307e-13, "14": 2.1445271137680707e-14, "15": 1.120542024705965e-15, "16": 5.493019963066202e-17, "17": 2.5255152901128702e-18, "18": 1.0061166817822486e-19, "2": 0.024842719904137597, "3": 0.005737116544141827, "4": 0.0010428405598219182, "5": 0.00015563066577862122, "6": 1.9656541877273517e-05, "7": 2.1492468111443617e-06, "8": 2.0701592058471582e-07, "9": 1.7809318706980092e-08}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:18.868010+00:00", "p_over_1_5": 0.814930416651792, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Estoril vs CS Maritimo

The model's most likely 1X2 outcome is **Estoril win** at **49.9%**. Expected goals are 2.02 for Estoril and 1.15 for CS Maritimo (3.17 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 51.3%; Under 3.5 goals: 70.4%; Double Chance 1X: 74.6%; Double Chance X2: 50.1%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 85.7%; BTTS Yes (both teams score): 52.8%; BTTS No (at least one team does not score): 47.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Estoril win | 49.9% | 2.00 |
| Draw | 24.7% | 4.05 |
| CS Maritimo win | 25.4% | 3.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Estoril expected goals | 2.02 |
| CS Maritimo expected goals | 1.15 |
| Expected total goals | 3.17 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 51.3% |
| Under 2.5 | 48.7% |
| Over 3.5 | 29.6% |
| Under 3.5 | 70.4% |
| Over 4.5 | 14.3% |
| Under 4.5 | 85.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.70% |
| 2 | 1-0 | 10.40% |
| 3 | 2-1 | 8.78% |
| 4 | 2-0 | 8.73% |
| 5 | 0-1 | 7.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Estoril win | 49.9% | 46.4% | 2.08 | +3.7% |
| Draw | 24.7% | 26.5% | 3.55 | -12.4% |
| CS Maritimo win | 25.4% | 27.0% | 3.49 | -11.2% |
| Over 2.5 | 51.3% | 51.3% | 1.87 | -4.2% |
| Under 2.5 | 48.7% | 48.7% | 1.96 | -4.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T15:30:00+00:00 |
| Fixture id | 88fe8a3db780908444b4b21229766ad5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T12:16:29Z |
| Market best draw last update utc | 2026-11-06T12:16:29Z |
| Market best away last update utc | 2026-11-06T12:16:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Estoril |
| Matched away-team name | Maritimo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 2.0189 |
| Dc lambda away | 1.1529 |
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
| P btts yes | 52.8% |
| P btts no | 47.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.82 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.37 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.01 |
| Fair Under 4.5 odds | 1.17 |
| Score matrix json | [[0.06320965062272434,0.07935528519428114,0.03670875796597746,0.012318540487380444,0.003100345424650573,0.0006242390005211262,0.0001047394930774885,1.5063408270098477e-05,1.895588562528423e-06,2.1203736064441694e-07,2.134632951370673e-08,1.953625626604422e-09,1.6389696704540783e-10,1.2692243168901892e-11,9.12685535794468e-13,6.125488492610351e-14,3.8541761991344205e-15],[0.10397360630578004,0.11695131045349774,0.06471427283670927,0.021716490402351338,0.00546563302100374,0.0011004777942222922,0.0001846464034026254,2.6555447981797145e-05,3.3417539088439023e-06,3.7380299330847005e-07,3.763167888961653e-08,3.4440680869138e-09,2.8893576438396535e-10,2.2375294966488405e-11,1.608983361198521e-12,1.0798690980945426e-13,6.794569577720515e-15],[0.08725596868884065,0.08784275818228138,0.05462138404251875,0.01914211979408388,0.004817712259215977,0.000970022198681397,0.0001627575868841631,2.3407445541848923e-05,2.945607345398311e-06,3.2949070244440253e-07,3.317065013781148e-08,3.0357927398594324e-09,2.546840171759157e-10,1.9722826697177e-11,1.4182472248561412e-12,9.518565502378282e-14,5.989110689445545e-15],[0.05127483537302368,0.05161965458856739,0.025983396343042,0.010771133175920303,0.0028310659623390325,0.0005700209314383345,9.564237952541772e-05,1.3755080995563095e-05,1.730947853521268e-06,1.9362092678181856e-07,1.949230122122259e-08,1.7839441278567861e-09,1.496617509273671e-10,1.1589862644178773e-11,8.334145396066952e-13,5.5934612434622844e-14,3.5194230176647056e-15],[0.022598242693627788,0.022750214089763816,0.01145160374076415,0.0038428716236268423,0.0011947653461919553,0.0002512240410988887,4.215225048676723e-05,6.062245862846385e-06,7.628767483955163e-07,8.533411491522162e-08,8.590798009392218e-09,7.862336770054169e-10,6.596008636215489e-11,5.107974056153811e-12,3.673089127135221e-13,2.4651935741497018e-14,1.551107378817058e-15],[0.007967738078531642,0.0080213204874055,0.004037631616872163,0.0013549281234648475,0.00034100997700320265,8.481717697238486e-05,1.4862133124799293e-05,2.137439970783315e-06,2.689767607076516e-07,3.0087289796189715e-08,3.0289624442217966e-09,2.7721199793408983e-10,2.3256352225970715e-11,1.8009807197461713e-12,1.29506583767986e-13,8.69183368724627e-15,5.468928488663853e-16],[0.0023410688369581486,0.0023568123398679296,0.0011863308582952719,0.00039810294651983533,0.00010019503934310237,2.0173768612819134e-05,4.181407725150301e-06,6.280194023887532e-07,7.903034790454319e-08,8.840202305366094e-09,8.899651967213035e-10,8.145001293943164e-11,6.833146486609387e-12,5.291614505151025e-13,3.805142996066145e-14,2.553821521325059e-15,1.6068723557643642e-16],[0.0005895851400476676,0.0005935500535185439,0.000298770815359579,0.00010026000849349746,2.5233562281723126e-05,5.080651198763038e-06,8.524696960903283e-07,1.514494295367983e-07,1.9903352691610312e-08,2.22635568505163e-09,2.2413277510808196e-10,2.0512731846098048e-11,1.7208898622171718e-12,1.3326636234889617e-13,9.583040578815608e-15,6.431657179562464e-16,4.046818478618682e-17],[0.00012992326534473308,0.00013079698903611364,6.583829422513345e-05,2.209368385016066e-05,5.560565531987634e-06,1.119591979145808e-06,1.878535244537086e-07,2.7016689222752473e-08,4.199802545279698e-09,4.906083630217204e-10,4.9390766548940474e-11,4.520265050049401e-12,3.7922195627221235e-13,2.9367091842889943e-14,2.1117559439000488e-15,1.4173048904846757e-16,8.917725961631859e-18],[2.5449239143869427e-05,2.5620383265814094e-05,1.2896339159226516e-05,4.327688673617362e-06,1.0891980094806596e-06,2.1930455600263895e-07,3.679656030162236e-08,5.2920020373648965e-09,6.659487916037496e-10,9.202059946290838e-11,9.674613904352334e-12,8.854249925688585e-13,7.428161713893347e-14,5.75239654950668e-15,4.1364864012000993e-16,2.776202630222947e-17,1.7467952334394e-18],[4.486474336640419e-06,4.5166455219804164e-06,2.273509803078673e-06,7.629329922749744e-07,1.9201591408802387e-07,3.866144118698252e-08,6.486906053913946e-09,9.329328549221414e-10,1.1740084433002216e-10,1.3132261747749756e-11,1.6331507049955161e-12,1.5609254499607128e-13,1.3095187918741968e-14,1.014096309427687e-15,7.292257335448435e-17,4.894198126472989e-18,3.0794445137977944e-19],[7.190231739182723e-07,7.238585479372144e-07,3.643632197321431e-07,1.2227117786285987e-07,3.077336046767067e-08,6.196061776948659e-09,1.0396216337855069e-09,1.4951614387279988e-10,1.8815203515477754e-11,2.1046371413467725e-12,2.1187906597891763e-13,2.395422348023967e-14,2.0986955176569233e-15,1.6252377531919946e-16,1.1686909633120179e-17,7.843668784510679e-19,4.9352605232422705e-20],[1.056311545962001e-07,1.0634151576264474e-07,5.352832702589635e-08,1.7962766931569415e-08,4.520891279888838e-09,9.102587832904301e-10,1.527300336114525e-10,2.196530443099542e-11,2.7641274209171787e-12,3.0919066215211446e-13,3.1126994491920875e-14,2.8487564608962016e-15,2.952302195310711e-16,2.3876245799904912e-17,1.7169151189948393e-18,1.1523074916528514e-19,7.250354177908361e-21],[1.4324486407158534e-08,1.4420817446157479e-08,7.2588981518902405e-09,2.435904556092764e-09,6.130714554296733e-10,1.2343886250306588e-10,2.0711496516301633e-11,2.9786828133582835e-12,3.7483927748345053e-13,4.192889355559157e-14,4.221086205103914e-15,3.863156978394011e-16,3.240947003134727e-17,3.1003827325242635e-18,2.328283485899839e-19,1.5626273388894685e-20,9.832099276539531e-22],[1.8037710363632578e-09,1.8159012540276225e-09,9.140565232235545e-10,3.0673449370091595e-10,7.719931473232286e-11,1.5543694804540193e-11,2.6080374872758906e-12,3.7508233332286553e-13,4.72005915463811e-14,5.279779088242817e-15,5.315285185341077e-16,4.864572780123826e-17,4.081072206345402e-18,3.160397764922161e-19,2.8073750938128085e-20,1.96769493467468e-21,1.238079704749994e-22],[2.119925188613093e-10,2.134181517965123e-10,1.0742668600026718e-10,3.604970732450006e-11,9.073034689296486e-12,1.8268100261048435e-12,3.065158631924013e-13,4.4082451163983653e-14,5.547362770518527e-15,6.205187051924996e-16,6.24691644444241e-17,5.717205876205956e-18,4.796378028235568e-19,3.714333301084091e-20,2.670937070702583e-21,2.214415583953785e-22,1.45508287842449e-23],[2.335774632726449e-11,2.351482532531182e-11,1.18364803336034e-11,3.972026576129717e-12,9.996845352344965e-13,2.0128146694542652e-13,3.3772511483834703e-14,4.857089850637551e-15,6.112191745023476e-16,6.836995279390636e-17,6.882973532304847e-18,6.299328168487417e-19,5.2847422104779973e-20,4.092524372446963e-21,2.942890196723072e-22,1.9751206004761862e-23,1.5351837630290374e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.16630947838483331, "-10": 2.5057047641874258e-08, "-11": 2.2631428310537616e-09, "-12": 1.8774799495656582e-10, "-13": 1.439993160814186e-11, "-14": 1.0266615562933677e-12, "-15": 6.804945450382402e-14, "-16": 3.8541761991344205e-15, "-2": 0.06385735255643372, "-3": 0.0188561783781452, "-4": 0.00437812976165376, "-5": 0.0008341122435971697, "-6": 0.00013444304431002574, "-7": 1.8754955211525204e-05, "-8": 2.3044139498731563e-06, "-9": 2.528597340997499e-07, "0": 0.2468373979684607, "1": 0.22200469636602738, "10": 5.266376176056892e-06, "11": 8.329395966426644e-07, "12": 1.2100307795744086e-07, "13": 1.6251786373762556e-08, "14": 2.0290256684933736e-09, "15": 2.355073441866211e-10, "16": 2.335774632726449e-11, "2": 0.1517876240972424, "3": 0.0784871749290622, "4": 0.03191194055713885, "5": 0.010646543839027097, "6": 0.0030049832411078526, "7": 0.0007340731059467282, "8": 0.00015794407657436228, "9": 3.034883957903674e-05} |
| Raw goal margin distribution | {"-1": 0.13606492874661724, "-10": 5.9132300913960415e-08, "-11": 6.09185250963967e-09, "-12": 5.767866714945065e-10, "-13": 5.051398262769629e-11, "-14": 4.11467003610113e-12, "-15": 3.1313139640930347e-13, "-16": 2.2201879779250123e-14, "-17": 1.3243722954729803e-15, "-2": 0.05685257006403735, "-3": 0.01859473258976037, "-4": 0.004835415787851702, "-5": 0.0010384722006929583, "-6": 0.00018945317369059448, "-7": 2.9994865931367146e-05, "-8": 4.190585430847427e-06, "-9": 5.235588909026272e-07, "0": 0.20358278390796541, "1": 0.2346028596020555, "10": 1.6033208283327323e-05, "11": 2.8924416181622115e-06, "12": 4.795677869567561e-07, "13": 7.354716952883404e-08, "14": 1.0490807850101672e-08, "15": 1.39804161449547e-09, "16": 1.735812439937307e-10, "17": 1.8131874423682274e-11, "2": 0.1743368655048524, "3": 0.09985012985439193, "4": 0.04546865280054383, "5": 0.017099865848053692, "6": 0.0054628500358310265, "7": 0.0015145509383794346, "8": 0.00037053669514297815, "9": 8.106653855432883e-05} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Estoril", "away_goals": 0.0, "away_xg": 0.63, "date": "2026-10-31T00:00:00+00:00", "home": "Porto", "home_goals": 4.0, "home_xg": 3.1, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 3.0, "away_xg": 1.33, "date": "2026-10-25T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 2.01, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 1.0, "away_xg": 1.36, "date": "2026-10-10T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 2.0, "home_xg": 0.73, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 2.0, "away_xg": 2.17, "date": "2026-09-20T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 0.95, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 0.0, "away_xg": 0.75, "date": "2026-09-14T00:00:00+00:00", "home": "Sp Braga", "home_goals": 1.0, "home_xg": 1.79, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": 1.08, "date": "2026-09-07T00:00:00+00:00", "home": "Estoril", "home_goals": 0.0, "home_xg": 0.87, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 1.0, "away_xg": 0.36, "date": "2026-08-31T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": 2.03, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 2.0, "away_xg": 0.71, "date": "2026-08-22T00:00:00+00:00", "home": "Estoril", "home_goals": 0.0, "home_xg": 1.16, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-08-16T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 2.08, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": 1.47, "date": "2026-08-07T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 1.22, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 57.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 21.8% |
| Raw p over 1 5 | 82.0% |
| Raw p under 3 5 | 60.9% |
| Raw p btts yes | 58.9% |
| P home draw | 74.6% |
| P draw away | 50.1% |
| P home away | 75.3% |
| Raw p home draw | 78.2% |
| Raw p draw away | 42.1% |
| Raw p home away | 79.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.8732 |
| Totals anchor target over 2 5 | 0.5125 |
| Totals anchor reference over odds | 1.87 |
| Totals anchor reference under odds | 1.96 |
| Totals anchor reference last update utc | 2026-11-06T12:16:29Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5971 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.49, "draw": 3.55, "home": 2.08}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.87, "under": 1.96}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.08 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.49 |
| Market reference 1x2 last update utc | 2026-11-06T12:16:29Z |
| Market reference home last update utc | 2026-11-06T12:16:29Z |
| Market reference draw last update utc | 2026-11-06T12:16:29Z |
| Market reference away last update utc | 2026-11-06T12:16:29Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.96 |
| Market reference over 2 5 last update utc | 2026-11-06T12:16:29Z |
| Market reference under 2 5 last update utc | 2026-11-06T12:16:29Z |
| Market best over 2 5 last update utc | 2026-11-06T12:16:29Z |
| Market best under 2 5 last update utc | 2026-11-06T12:16:29Z |
| Home probability edge | +3.4% |
| Draw probability edge | -1.9% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.1143 |
| Raw ev home | 0.2039 |
| Raw edge prob draw | -0.0618 |
| Raw ev draw | -0.2773 |
| Raw edge prob away | -0.0525 |
| Raw ev away | -0.2405 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,378.3893 |
| Elo away rating | 1,388.6236 |
| Elo rating diff | 49.7657 |
| Elo home expectancy | 0.5711 |
| Research p home | 0.5739 |
| Research p draw | 0.2133 |
| Research p away | 0.2127 |
| Research p over 1 5 | 0.8251 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.018919791750785, 1.152920867621097], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:18.484557+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T12:17:18.065934+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:18.485958+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Estoril%22+%22CS+Maritimo%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:18.568253+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Estoril_vs_CS+Maritimo&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 2.1741572673293668, "goals_for": 0.5196294860897706, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 0.13586574280159558, "results": "LLLLLDLLLD", "xg_against": 1.7383780696529123, "xg_for": 1.0563300250269338, "xg_matches": 10}, "venue": {"goals_against": 1.7177832069357093, "goals_for": 0.6329817884866369, "last_match": "2026-10-25T00:00:00+00:00", "matches": 5, "points_per_game": 0.34490701073453883, "results": "LLDLD", "xg_against": 1.3851867116529304, "xg_for": 1.284754675915346, "xg_matches": 5}}}, "goal_rates": [2.018919791750785, 1.152920867621097], "h2h": [], "margin_distribution": {"-1": 0.13118542479670148, "-10": 5.913230091396042e-08, "-11": 6.091852509639672e-09, "-12": 5.767866714945066e-10, "-13": 5.0513982627696295e-11, "-14": 4.114670036101131e-12, "-15": 3.131313964093035e-13, "-16": 2.2201879779250126e-14, "-17": 1.3243722954729803e-15, "-2": 0.05685257006403735, "-3": 0.018594732589760375, "-4": 0.004835415787851703, "-5": 0.0010384722006929585, "-6": 0.0001894531736905945, "-7": 2.9994865931367153e-05, "-8": 4.190585430847428e-06, "-9": 5.235588909026272e-07, "0": 0.21334179180779694, "1": 0.22972335565213975, "10": 1.6033208283327326e-05, "11": 2.892441618162212e-06, "12": 4.795677869567562e-07, "13": 7.354716952883404e-08, "14": 1.0490807850101674e-08, "15": 1.39804161449547e-09, "16": 1.7358124399373072e-10, "17": 1.8131874423682274e-11, "2": 0.1743368655048524, "3": 0.09985012985439194, "4": 0.045468652800543845, "5": 0.017099865848053696, "6": 0.005462850035831028, "7": 0.0015145509383794346, "8": 0.00037053669514297826, "9": 8.106653855432884e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:18.568654+00:00", "p_over_1_5": 0.8250899287689788, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Rio Ave FC vs Braga

The model's most likely 1X2 outcome is **Braga win** at **63.0%**. Expected goals are 0.96 for Rio Ave FC and 1.97 for Braga (2.93 combined). The most likely exact score is 0-1 at 12.5%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 53.2%; Under 3.5 goals: 69.0%; Double Chance 1X: 37.0%; Double Chance X2: 84.1%; Double Chance 12 (either team wins): 78.9%; Under 4.5 goals: 84.7%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rio Ave FC win | 15.9% | 6.29 |
| Draw | 21.1% | 4.74 |
| Braga win | 63.0% | 1.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rio Ave FC expected goals | 0.96 |
| Braga expected goals | 1.97 |
| Expected total goals | 2.93 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 76.6% |
| Under 1.5 | 23.4% |
| Over 2.5 | 53.2% |
| Under 2.5 | 46.8% |
| Over 3.5 | 31.0% |
| Under 3.5 | 69.0% |
| Over 4.5 | 15.3% |
| Under 4.5 | 84.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.52% |
| 2 | 0-2 | 11.22% |
| 3 | 1-2 | 10.31% |
| 4 | 1-1 | 10.01% |
| 5 | 0-3 | 7.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rio Ave FC win | 15.9% | 14.8% | 6.07 | -3.5% |
| Draw | 21.1% | 21.4% | 4.29 | -9.5% |
| Braga win | 63.0% | 63.8% | 1.53 | -3.6% |
| Over 2.5 | 53.2% | 53.2% | 1.81 | -3.7% |
| Under 2.5 | 46.8% | 46.8% | 2.04 | -4.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T20:30:00+00:00 |
| Fixture id | 3642cddab8c2e0da43a419cdd01d1db0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T12:16:29Z |
| Market best draw last update utc | 2026-11-06T12:16:29Z |
| Market best away last update utc | 2026-11-06T12:16:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Rio Ave |
| Matched away-team name | Sp Braga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 0.9638 |
| Dc lambda away | 1.9670 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.91 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.28 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.22 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.53 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.05584058352037414,0.12517562980959618,0.11223651291153629,0.07017272715229322,0.032905144958517665,0.012343810579186558,0.0038588104232870216,0.0010339769268408626,0.00024242438652570829,5.052301278621921e-05,9.476428389984578e-06,1.6158738199073523e-06,2.525699296410473e-07,3.6441289435224816e-08,4.8822627088604085e-09,6.104995247397097e-10,7.156831497751571e-11],[0.05273756783144506,0.10006696066782142,0.10314613837524796,0.06448922580768268,0.030240057777133577,0.011344048037933634,0.0035462736996999256,0.0009502320092286036,0.00022278970247252878,4.6431001220514104e-05,8.708903801981977e-06,1.4849993135163849e-06,2.3211352737513976e-07,3.348979922087203e-08,4.486833490179355e-09,5.610533223395677e-10,6.577178075527508e-11],[0.022155299566378617,0.041555936239952615,0.04539221395064202,0.0296330242107341,0.013895412032331194,0.005212629643877212,0.001629525135167282,0.00043663492285142595,0.00010237264542388406,2.133520702201091e-05,4.001771675515166e-06,6.823623645534938e-07,1.0665697549011353e-07,1.5388679561516742e-08,2.061715639764711e-09,2.578059586880723e-10,3.0222362682976614e-11],[0.006786958288758068,0.012730065105454524,0.011938673459769043,0.00869386934024721,0.004256660199334592,0.0015968143360799133,0.0004991816558258763,0.00013375684675032856,3.136039177985661e-05,6.535734698895552e-06,1.225885362618652e-06,2.0903192449136784e-07,3.2672834853246494e-08,4.714101291664435e-09,6.315770187823478e-10,7.897515819937217e-11,9.258187383227883e-12],[0.0015593155040175006,0.002924754660562348,0.0027429310496951144,0.0017149405942388687,0.0009366285230206215,0.0003668708787279801,0.00011468785605176472,3.0730868827019985e-05,7.205104707272577e-06,1.5015964460859927e-06,2.81649300135771e-07,4.8025449225745824e-08,7.50664079242387e-09,1.0830729936527108e-09,1.4510592160257385e-10,1.814468033736072e-11,2.127084698557672e-12],[0.0002866043653277596,0.0005375739874773097,0.0005041545541041774,0.0003152084740517821,0.00014780643352106193,6.458053275400867e-05,2.107978796454561e-05,5.648376568722838e-06,1.3243082983703431e-06,2.7599552194541973e-07,5.176753434596412e-08,8.827144576875154e-09,1.3797310515498905e-09,1.9907032742873819e-10,2.667067085465122e-11,3.3350175630049932e-12,3.9096113548401457e-13],[4.389856853498259e-05,8.233904080598751e-05,7.722025873631107e-05,4.827979778027899e-05,2.2639190594377277e-05,8.492710812105295e-06,3.0922412943848366e-06,8.651495786880574e-07,2.0284142752317622e-07,4.2273635021621904e-08,7.929120869371705e-09,1.3520345746758303e-09,2.1133041032728474e-10,3.0491169951016315e-11,4.085088763557183e-12,5.108174011499091e-13,5.988266850343506e-14],[5.763298676956167e-06,1.0810021847542138e-05,1.0137993785709464e-05,6.338495854347875e-06,2.9722248709763036e-06,1.1149800692970864e-06,3.4855498515308645e-07,1.0878062466574529e-07,2.6630383857383002e-08,5.549966500526987e-09,1.040988199409259e-09,1.7750417235629565e-10,2.7744874488771914e-11,4.00308541490367e-12,5.363178675745619e-13,6.70635364765346e-14,7.861798588795121e-15],[6.620639614175221e-07,1.2418106866489131e-06,1.1646108770017644e-06,7.281402387728468e-07,3.414369239911634e-07,1.2808430778227159e-07,4.004055787789829e-08,1.072895748745196e-08,2.929852975310545e-09,6.375572416132453e-10,1.195844272040717e-10,2.0390946592484144e-11,3.1872166519000604e-12,4.598579279398999e-13,6.160998273525935e-14,7.70398223570336e-15,9.03130968793268e-16],[6.760459993131902e-08,1.2680363160319039e-07,1.1892061342048322e-07,7.435177324972972e-08,3.486476835075149e-08,1.307893026915516e-08,4.088616892190345e-09,1.0955540867476723e-09,2.5686165763582204e-10,6.234979951305108e-11,1.2210991430250728e-11,2.0821580193766753e-12,3.254527042746826e-13,4.695696043787028e-14,6.291111550121065e-15,7.8666815787344e-16,9.222040677177018e-17],[6.212909897526189e-09,1.1653342207927997e-08,1.0928887337409179e-08,6.832979832602581e-09,3.2040965345760824e-09,1.201962816152169e-09,3.7574674478495273e-10,1.00682184877136e-10,2.3605765534325315e-11,4.919613950606968e-12,1.0747546040645725e-12,1.9135177458251507e-13,2.990933057246166e-14,4.3153774234086774e-15,5.781575404025304e-16,7.229535252166133e-17,8.475119719195168e-18],[5.190643217929739e-10,9.73591162522422e-10,9.130657916032016e-10,5.708687396299034e-10,2.6768973349205764e-10,1.004192921315046e-10,3.1392170893284234e-11,8.411602754885297e-12,1.9721693827166727e-12,4.1101450381114203e-13,7.709258212870726e-14,1.5310811046618018e-14,2.498807586934143e-15,3.605329052742624e-16,4.8302801191117454e-17,6.0399939391334016e-18,7.080631043611164e-19],[3.9751977745061516e-11,7.456142254526992e-11,6.992615270148346e-11,4.3719362861873374e-11,2.050072771636558e-11,7.690502503037642e-12,2.404135338002911e-12,6.44193467887518e-13,1.5103645178393394e-13,3.147709970117075e-14,5.90405173390436e-15,1.0067297757747513e-15,1.8327783989184112e-16,2.761102126480011e-17,3.699217606289778e-18,4.625663806353863e-19,5.422624438804815e-20],[2.8101803749522003e-12,5.2709590377869095e-12,4.943278628244652e-12,3.0906461134531537e-12,1.4492547533166778e-12,5.436634963462171e-13,1.6995516522254483e-13,4.553986855043461e-14,1.0677196375678555e-14,2.2252057094601526e-15,4.1737421020220147e-16,7.116859133162753e-17,1.1124040679310114e-17,1.8693796295532978e-18,2.6150821442247976e-19,3.270013314333075e-20,3.833407453685396e-21],[1.8446966925656917e-13,3.460034377266669e-13,3.244933961261716e-13,2.0288038142302583e-13,9.513394492244494e-14,3.5687896140674786e-14,1.1156427322776985e-14,2.989389778807063e-15,7.008869969929827e-16,1.4606996935523248e-16,2.7397843639674372e-17,4.6717451382901254e-18,7.302193564510469e-19,1.0535749428862954e-19,1.6440525211396947e-20,2.1465464634805165e-21,2.516377281010085e-22],[1.1301927532365776e-14,2.1198638209175228e-14,1.988077965623963e-14,1.2429899060493446e-14,5.8285839385666956e-15,2.186495035145943e-15,6.83522302773581e-16,1.8315133746503008e-16,4.2941335994779376e-17,8.949288058903688e-18,1.6785872962563542e-18,2.862244249443564e-19,4.4738445526575973e-20,6.454951484656215e-21,8.648093799495858e-22,1.2595268274717218e-22,1.5417121843760683e-23],[6.491593905804391e-16,1.2176060253080403e-15,1.1419109500525177e-15,7.139477470527769e-16,3.3478183138862096e-16,1.2558776195102568e-16,3.926011029941152e-17,1.0519834804488762e-17,2.4664617097616232e-18,5.14028635010248e-19,9.641458973730887e-20,1.644014020918265e-20,2.5696839720816133e-21,3.707590904300017e-22,4.967286584068246e-23,6.2113128269728775e-24,8.480895458843424e-25]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.26260029569153, "-10": 1.1072947281104574e-05, "-11": 1.864026139504264e-06, "-12": 2.8820254674458195e-07, "-13": 4.119518707147547e-08, "-14": 5.473538393882953e-09, "-15": 6.762713054949848e-10, "-16": 7.156831497751571e-11, "-2": 0.19233850983334147, "-3": 0.10615669474159926, "-4": 0.046019964188457926, "-5": 0.016359634337743865, "-6": 0.004918241504479019, "-7": 0.0012793771579135821, "-8": 0.0002930739012104042, "-9": 5.994806204995163e-05, "0": 0.2109980405500715, "1": 0.10810377681554077, "10": 7.259615218563616e-09, "11": 5.987778575196119e-10, "12": 4.536019485986649e-11, "13": 3.1767785400821595e-12, "14": 2.068102184157969e-13, "15": 1.2519533557673817e-14, "16": 6.491593905804391e-16, "2": 0.03796729952637842, "3": 0.010267251801686778, "4": 0.0021808031462513667, "5": 0.00037984563893658573, "6": 5.595085999898807e-05, "7": 7.131138510082171e-06, "8": 8.003884048310095e-07, "9": 8.021621293040368e-08} |
| Raw goal margin distribution | {"-1": 0.2463860348637257, "-10": 1.5129636517770273e-05, "-11": 2.667633235063107e-06, "-12": 4.3207815078141484e-07, "-13": 6.470903831629991e-08, "-14": 9.008832330615398e-09, "-15": 1.1653429748598174e-09, "-16": 1.2808955333176905e-10, "-2": 0.1860191608526886, "-3": 0.10652068006379466, "-4": 0.048084600473011475, "-5": 0.017836779164447557, "-6": 0.005602755078265824, "-7": 0.0015240974475164396, "-8": 0.00036531876686745485, "-9": 7.822333960689279e-05, "0": 0.20371484383258076, "1": 0.12329950936012547, "10": 1.2063188946849085e-08, "11": 1.0421329292370126e-09, "12": 8.270326755125277e-11, "13": 6.068602226915208e-12, "14": 4.139573463115969e-13, "15": 2.6236398347205022e-14, "16": 1.412952390568093e-15, "2": 0.04465647185564165, "3": 0.012529219600368286, "4": 0.0027711463746865686, "5": 0.0005036551201115845, "6": 7.751429820815843e-05, "7": 1.03313311174442e-05, "8": 1.2133298767313546e-06, "9": 1.2729361662610104e-07} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Rio Ave", "away_goals": 1.0, "away_xg": 1.08, "date": "2026-11-01T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 2.0, "home_xg": 0.86, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.65, "date": "2026-10-25T00:00:00+00:00", "home": "Rio Ave", "home_goals": 0.0, "home_xg": 0.58, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.21, "date": "2026-10-11T00:00:00+00:00", "home": "Rio Ave", "home_goals": 3.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 0.0, "away_xg": 0.29, "date": "2026-09-19T00:00:00+00:00", "home": "Alverca", "home_goals": 1.0, "home_xg": 3.3, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 3.0, "away_xg": 1.87, "date": "2026-09-14T00:00:00+00:00", "home": "Rio Ave", "home_goals": 3.0, "home_xg": 1.24, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-09-06T00:00:00+00:00", "home": "Santa Clara", "home_goals": 4.0, "home_xg": 1.8, "source": "pipeline training history"}, {"away": "Sp Lisbon", "away_goals": 4.0, "away_xg": 1.66, "date": "2026-08-28T00:00:00+00:00", "home": "Rio Ave", "home_goals": 0.0, "home_xg": 0.47, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 2.0, "away_xg": 0.71, "date": "2026-08-22T00:00:00+00:00", "home": "Estoril", "home_goals": 0.0, "home_xg": 1.16, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 2.0, "away_xg": 1.98, "date": "2026-08-15T00:00:00+00:00", "home": "Rio Ave", "home_goals": 0.0, "home_xg": 0.57, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 0.0, "away_xg": 0.3, "date": "2026-08-09T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": 1.53, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 18.4% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 61.2% |
| Raw p over 1 5 | 78.5% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 52.7% |
| P home draw | 37.0% |
| P draw away | 84.1% |
| P home away | 78.9% |
| Raw p home draw | 38.8% |
| Raw p draw away | 81.6% |
| Raw p home away | 79.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9536 |
| Totals anchor target over 2 5 | 0.5318 |
| Totals anchor reference over odds | 1.81 |
| Totals anchor reference under odds | 2.04 |
| Totals anchor reference last update utc | 2026-11-06T12:16:29Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5608 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.94, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.9, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.53, "draw": 4.29, "home": 6.07}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.81, "under": 2.04}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.07 |
| Reference draw odds | 4.29 |
| Reference away odds | 1.53 |
| Market reference 1x2 last update utc | 2026-11-06T12:16:29Z |
| Market reference home last update utc | 2026-11-06T12:16:29Z |
| Market reference draw last update utc | 2026-11-06T12:16:29Z |
| Market reference away last update utc | 2026-11-06T12:16:29Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-11-06T12:16:29Z |
| Market reference under 2 5 last update utc | 2026-11-06T12:16:29Z |
| Market best over 2 5 last update utc | 2026-11-06T12:16:29Z |
| Market best under 2 5 last update utc | 2026-11-06T12:16:29Z |
| Home probability edge | +1.1% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0356 |
| Raw ev home | 0.1160 |
| Raw edge prob draw | -0.0104 |
| Raw ev draw | -0.1261 |
| Raw edge prob away | -0.0251 |
| Raw ev away | -0.0630 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,370.7424 |
| Elo away rating | 1,556.2873 |
| Elo rating diff | -125.5450 |
| Elo home expectancy | 0.3268 |
| Research p home | 0.1788 |
| Research p draw | 0.2138 |
| Research p away | 0.6074 |
| Research p over 1 5 | 0.7903 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [0.9637701828400064, 1.96702609937485], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:18.484557+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T12:17:18.065934+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:18.892249+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Rio+Ave+FC%22+%22Braga%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:18.974191+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Rio+Ave+FC_vs_Braga&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 2.4282556797589714, "goals_for": 0.9932190408992481, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.6877582038772015, "results": "LLWLDLLWLL", "xg_against": 1.6602815864442582, "xg_for": 0.8033264458802587, "xg_matches": 10}, "venue": {"goals_against": 3.0556255141047255, "goals_for": 1.264779647458062, "last_match": "2026-10-25T00:00:00+00:00", "matches": 5, "points_per_game": 0.8723623359830545, "results": "LWDLL", "xg_against": 1.644775250533017, "xg_for": 0.9326370029898359, "xg_matches": 5}}}, "goal_rates": [0.9637701828400064, 1.96702609937485], "h2h": [], "margin_distribution": {"-1": 0.24132866216547352, "-10": 1.5129636517770273e-05, "-11": 2.667633235063107e-06, "-12": 4.3207815078141484e-07, "-13": 6.470903831629991e-08, "-14": 9.008832330615398e-09, "-15": 1.1653429748598174e-09, "-16": 1.2808955333176905e-10, "-2": 0.1860191608526886, "-3": 0.10652068006379466, "-4": 0.048084600473011475, "-5": 0.017836779164447557, "-6": 0.005602755078265824, "-7": 0.0015240974475164396, "-8": 0.00036531876686745485, "-9": 7.822333960689279e-05, "0": 0.21382958922908513, "1": 0.11824213666187329, "10": 1.2063188946849085e-08, "11": 1.0421329292370126e-09, "12": 8.270326755125277e-11, "13": 6.068602226915208e-12, "14": 4.139573463115969e-13, "15": 2.6236398347205022e-14, "16": 1.412952390568093e-15, "2": 0.04465647185564165, "3": 0.012529219600368286, "4": 0.0027711463746865686, "5": 0.0005036551201115845, "6": 7.751429820815843e-05, "7": 1.03313311174442e-05, "8": 1.2133298767313546e-06, "9": 1.2729361662610104e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:18.974593+00:00", "p_over_1_5": 0.7902741884097798, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Santa Clara vs Gil Vicente

The model's most likely 1X2 outcome is **Santa Clara win** at **41.7%**. Expected goals are 1.02 for Santa Clara and 0.85 for Gil Vicente (1.88 combined). The most likely exact score is 1-0 at 17.3%. Goal-market probabilities: at least one goal: 85.2%; Over 2.5 goals: 28.9%; Under 3.5 goals: 87.8%; Double Chance 1X: 72.6%; Double Chance X2: 58.3%; Double Chance 12 (either team wins): 69.1%; Under 4.5 goals: 95.8%; BTTS Yes (both teams score): 36.2%; BTTS No (at least one team does not score): 63.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Santa Clara win | 41.7% | 2.40 |
| Draw | 30.9% | 3.23 |
| Gil Vicente win | 27.4% | 3.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Santa Clara expected goals | 1.02 |
| Gil Vicente expected goals | 0.85 |
| Expected total goals | 1.88 |
| Over 0.5 | 85.2% |
| Under 0.5 | 14.8% |
| Over 1.5 | 55.4% |
| Under 1.5 | 44.6% |
| Over 2.5 | 28.9% |
| Under 2.5 | 71.1% |
| Over 3.5 | 12.2% |
| Under 3.5 | 87.8% |
| Over 4.5 | 4.2% |
| Under 4.5 | 95.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.32% |
| 2 | 0-0 | 14.82% |
| 3 | 1-1 | 12.84% |
| 4 | 0-1 | 12.50% |
| 5 | 2-0 | 8.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Santa Clara win | 41.7% | 42.6% | 2.26 | -5.9% |
| Draw | 30.9% | 31.1% | 3.06 | -5.4% |
| Gil Vicente win | 27.4% | 26.3% | 3.59 | -1.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T15:30:00+00:00 |
| Fixture id | 3145127655251c9de0251675640e2101 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T12:16:29Z |
| Market best draw last update utc | 2026-11-06T12:16:29Z |
| Market best away last update utc | 2026-11-06T12:16:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Santa Clara |
| Matched away-team name | Gil Vicente |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0243 |
| Dc lambda away | 0.8519 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 36.2% |
| P btts no | 63.8% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.75 |
| Fair Over 1.5 odds | 1.81 |
| Fair Under 1.5 odds | 2.24 |
| Fair Over 2.5 odds | 3.46 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.22 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.72 |
| Fair Under 4.5 odds | 1.04 |
| Score matrix json | [[0.14818428554767213,0.12503294523646988,0.05066261747027535,0.0143863756496095,0.00306391301909799,0.000522025183673164,7.411826279292431e-05,9.020117996365994e-06,9.605218727767617e-07,9.091797970854582e-08,7.745238647557805e-09,5.998285677619235e-10,4.2582477633796324e-11,2.7904394415148504e-12],[0.17317157852511214,0.1284454542563541,0.05189450357989968,0.014736187349350232,0.0031384135498204392,0.0005347184791393599,7.592048429199429e-05,9.239446539219413e-06,9.838774278615e-07,9.312869447044647e-08,7.93356788086775e-09,6.144136902383788e-10,4.3617891225311595e-11,2.858290329593558e-12],[0.08506773452254748,0.0724686038115179,0.02949537402017583,0.00754725244509531,0.0016073627985360114,0.00027386020911983886,3.888326384034735e-05,4.732054080971347e-06,5.039004422965081e-07,4.7696581916868943e-08,4.063238215402365e-09,3.1467672852002e-10,2.2339240700183516e-11,1.4638955224580834e-12],[0.029045399245340275,0.024743571017516865,0.010539436926437197,0.0028597637943169503,0.0005488155347925891,9.350641763228995e-05,1.3276243084920116e-05,1.6157054234931391e-06,1.7205100862920364e-07,1.6285449144602994e-08,1.3873459409454992e-09,1.0744274858593968e-10,7.627476723299884e-12,4.998302839720165e-13],[0.007437913052959037,0.006336305736184125,0.0026989271114447487,0.0007663989982148197,0.00015596564520428476,2.394501787935402e-05,3.3997653432643545e-06,4.137480210764973e-07,4.405862808249134e-08,4.1703594343044165e-09,3.552699825527008e-10,2.7513817778950445e-11,1.9532356295799574e-12,1.2799597492246932e-13],[0.0015237539030833957,0.001298075216515097,0.0005529105665688641,0.00015700687229523968,3.3438262132846354e-05,5.443869462467725e-06,6.964864572201192e-07,8.476170096631217e-08,9.025986997587672e-09,8.543527492236488e-10,7.278170888911964e-11,5.636565919888275e-12,4.001459002038169e-13,2.6221651823354697e-14],[0.0002601341196818398,0.0002216064241382208,9.43924758493674e-05,2.6804095087713036e-05,5.70855494841841e-06,9.72615549750097e-07,1.319544276596026e-07,1.4470453804245444e-08,1.5409097080086007e-09,1.4585445843146097e-10,1.2425238571989311e-11,9.622702922248375e-13,6.831260696571962e-14,4.476540667012658e-15],[3.806562956264743e-05,3.2427841685149535e-05,1.3812524952811878e-05,3.9222642366897914e-06,8.353373185735275e-07,1.4232359549350764e-07,2.0207411409151793e-08,2.349885235592864e-09,2.2548252496167048e-10,2.134299718738566e-11,1.818194896107211e-12,1.408097658537497e-13,9.996237304034614e-15,6.550557034234614e-16],[4.873901725391866e-06,4.152042547460559e-06,1.7685478993256373e-06,5.022044991843195e-07,1.0695611881524782e-07,1.8223032841165928e-08,2.5873455519940272e-09,3.148773500204973e-10,3.2039478894514984e-11,2.7327453141273605e-12,2.328006483289934e-13,1.8029202948479597e-14,1.2799125826456538e-15,8.387296256033188e-17],[5.547125565727372e-07,4.7255571947656554e-07,2.0128344433891767e-07,5.715731612181143e-08,1.2172978745141482e-08,2.07401496898655e-09,2.9447312374118774e-10,3.583708282970671e-11,3.816169802691474e-12,3.4515899065182e-13,2.6495700997332664e-14,2.0519546400406256e-15,1.456704753011618e-16,9.545819368245571e-18],[5.682006613607902e-08,4.840461409335349e-08,2.061777488884985e-08,5.8547123978367096e-09,1.2468970625894377e-09,2.1244456486281296e-10,3.016333805322482e-11,3.670847887578096e-12,3.9089618218693497e-13,3.7000189342361434e-14,3.0118820180631646e-15,2.1018489120870353e-16,1.492125235423754e-17,9.777930594863962e-19],[5.291061235972922e-09,4.507417795998446e-09,1.9199187347855017e-09,5.451884153350891e-10,1.1611054266137719e-10,1.9782750679077833e-11,2.808797658537502e-12,3.4182784853861217e-13,3.6400092036250213e-14,3.4454424442973117e-15,2.93514814814998e-16,2.1720576631170394e-17,1.3894608945825487e-18,9.105168835005599e-20],[4.5164299629268866e-10,3.8475148710944595e-10,1.6388354081438747e-10,4.653707800089854e-11,9.911152233926408e-12,1.688648154526038e-12,2.397579112970708e-13,2.917829653541592e-14,3.107098160348303e-15,2.941016706661315e-16,2.505431415498699e-17,1.940326703888174e-18,1.3162173880008072e-19,7.772137858534102e-21],[3.558653190346591e-11,3.031591585238073e-11,1.2912957582684798e-11,3.6668192013760815e-12,7.809343620246439e-13,1.3305449640101611e-13,1.8891364705127122e-14,2.29906007415082e-15,2.4481913528617927e-16,2.3173299645812168e-17,1.9741170732515917e-18,1.5288512988766814e-19,1.0853480434039002e-20,6.796098808744459e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.18504817299928986, "-10": 8.382491408780342e-09, "-11": 6.449103545096932e-10, "-12": 4.544076796338988e-11, "-13": 2.7904394415148504e-12, "-2": 0.06710316012532569, "-3": 0.017812348573333605, "-4": 0.0036391753930493593, "-5": 0.0006028540171682524, "-6": 8.387825619910098e-05, "-7": 1.0053107270525528e-05, "-8": 1.057823227668478e-06, "-9": 9.917397979063182e-08, "0": 0.3091464214698863, "1": 0.25698044966510686, "10": 6.149503429209324e-08, "11": 5.688725680665053e-09, "12": 4.819589121450693e-10, "13": 3.558653190346591e-11, "2": 0.11267309302592525, "3": 0.03596227350171306, "4": 0.008834412070202271, "5": 0.0017596874449351436, "6": 0.0002943889335043071, "7": 4.242492808492693e-05, "8": 5.367630452379347e-06, "9": 6.05084407413239e-07} |
| Raw goal margin distribution | {"-1": 0.20300664965212806, "-10": 9.195991881750568e-09, "-11": 7.07497341221961e-10, "-12": 4.985068435073357e-11, "-13": 3.0612448255906816e-12, "-2": 0.07361535916469125, "-3": 0.019540993827170592, "-4": 0.003992348543977531, "-5": 0.0006613595382815432, "-6": 9.201843765140918e-05, "-7": 1.1028736963486098e-05, "-8": 1.1604824078646923e-06, "-9": 1.0879857414231962e-07, "0": 0.3056053005444338, "1": 0.24274244695856334, "10": 5.808790170348256e-08, "11": 5.373541814562999e-09, "12": 4.552559769431624e-10, "13": 3.3614859979713164e-11, "2": 0.10643043991535449, "3": 0.033969783613403956, "4": 0.008344941438758594, "5": 0.001662191955934685, "6": 0.00027807831362068125, "7": 4.007437479698113e-05, "8": 5.07023686851607e-06, "9": 5.715597037182141e-07} |
| Research history json | {"away": [{"away": "Guimaraes", "away_goals": 0.0, "away_xg": 0.42, "date": "2026-11-02T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": 0.65, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 1.0, "away_xg": 1.08, "date": "2026-10-24T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": 0.35, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 2.0, "away_xg": 1.52, "date": "2026-10-19T00:00:00+00:00", "home": "Sp Braga", "home_goals": 1.0, "home_xg": 1.35, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": 1.49, "date": "2026-10-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 0.0, "home_xg": 1.09, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": 1.2, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": 1.1, "date": "2026-09-13T00:00:00+00:00", "home": "Benfica", "home_goals": 3.0, "home_xg": 2.91, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 1.0, "away_xg": 0.33, "date": "2026-09-06T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": 1.88, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 0.0, "away_xg": 0.27, "date": "2026-08-30T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": 0.23, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.76, "date": "2026-08-24T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 2.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 0.0, "away_xg": 0.3, "date": "2026-08-09T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": 1.53, "source": "pipeline training history"}], "h2h": [{"away": "Gil Vicente", "away_goals": 0.0, "away_xg": null, "date": "2026-03-21T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 0.0, "away_xg": null, "date": "2025-11-03T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": null, "date": "2025-03-15T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": null, "date": "2024-10-25T00:00:00+00:00", "home": "Santa Clara", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 2.0, "away_xg": null, "date": "2023-05-06T00:00:00+00:00", "home": "Santa Clara", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 0.0, "away_xg": null, "date": "2022-12-29T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Santa Clara", "away_goals": 2.0, "away_xg": 0.82, "date": "2026-11-01T00:00:00+00:00", "home": "Maritimo", "home_goals": 0.0, "home_xg": 2.06, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 2.0, "away_xg": 1.81, "date": "2026-10-26T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": 1.56, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 0.61, "date": "2026-10-10T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.43, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 0.0, "away_xg": 0.5, "date": "2026-09-20T00:00:00+00:00", "home": "Santa Clara", "home_goals": 0.0, "home_xg": 1.04, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 2.0, "away_xg": 1.16, "date": "2026-09-13T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.72, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-09-06T00:00:00+00:00", "home": "Santa Clara", "home_goals": 4.0, "home_xg": 1.8, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 1.41, "date": "2026-08-29T00:00:00+00:00", "home": "Alverca", "home_goals": 1.0, "home_xg": 0.41, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 0.0, "away_xg": 1.05, "date": "2026-08-23T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": 1.36, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 1.26, "date": "2026-08-15T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 0.0, "home_xg": 0.69, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.24, "date": "2026-08-10T00:00:00+00:00", "home": "Santa Clara", "home_goals": 2.0, "home_xg": 1.44, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 39.3% |
| Unadjusted draw probability | 30.6% |
| Unadjusted away-win probability | 30.1% |
| Raw p over 1 5 | 55.3% |
| Raw p under 3 5 | 87.9% |
| Raw p btts yes | 36.1% |
| P home draw | 72.6% |
| P draw away | 58.3% |
| P home away | 69.1% |
| Raw p home draw | 69.9% |
| Raw p draw away | 60.7% |
| Raw p home away | 69.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.2894 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.59, "draw": 3.06, "home": 2.26}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.26 |
| Reference draw odds | 3.06 |
| Reference away odds | 3.59 |
| Market reference 1x2 last update utc | 2026-11-06T12:16:29Z |
| Market reference home last update utc | 2026-11-06T12:16:29Z |
| Market reference draw last update utc | 2026-11-06T12:16:29Z |
| Market reference away last update utc | 2026-11-06T12:16:29Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 2.53 |
| Reference Under 2.5 odds | 1.51 |
| Market reference over 2 5 last update utc | 2026-11-06T12:15:58Z |
| Market reference under 2 5 last update utc | 2026-11-06T12:15:58Z |
| Home probability edge | -1.0% |
| Draw probability edge | -0.2% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | -0.0330 |
| Raw ev home | -0.1107 |
| Raw edge prob draw | -0.0051 |
| Raw ev draw | -0.0648 |
| Raw edge prob away | 0.0380 |
| Raw ev away | 0.0803 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,480.8777 |
| Elo away rating | 1,467.9622 |
| Elo rating diff | 72.9156 |
| Elo home expectancy | 0.6034 |
| Research p home | 0.4001 |
| Research p draw | 0.3088 |
| Research p away | 0.2911 |
| Research p over 1 5 | 0.5865 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.0243154848907499, 0.8518929558693003], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:18.484557+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T12:17:18.065934+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:18.581618+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Santa+Clara%22+%22Gil+Vicente%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:18.664365+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Santa+Clara_vs_Gil+Vicente&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 0.7142214406459612, "goals_for": 0.7243555948174364, "last_match": "2026-11-02T00:00:00+00:00", "matches": 10, "points_per_game": 1.390678704648646, "results": "DLWWDLLDWW", "xg_against": 0.9698401540895999, "xg_for": 1.0809685833604397, "xg_matches": 10}, "venue": {"goals_against": 0.9955634945558121, "goals_for": 1.1034760336115474, "last_match": "2026-10-19T00:00:00+00:00", "matches": 4, "points_per_game": 1.9072673778740439, "results": "WWLD", "xg_against": 1.4159916672192816, "xg_for": 1.1644490402329988, "xg_matches": 4}}, "home": {"all": {"goals_against": 0.5739054067991304, "goals_for": 1.4663234401593819, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 2.0720961954158974, "results": "WLWDWWDWWD", "xg_against": 1.0399163493907206, "xg_for": 1.1824774148588095, "xg_matches": 10}, "venue": {"goals_against": 0.8151944568095735, "goals_for": 1.5119397621276964, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 1.4751375496189745, "results": "LDWWD", "xg_against": 1.0078220045059325, "xg_for": 1.437884392379623, "xg_matches": 5}}}, "goal_rates": [1.0898686687338939, 0.8825907528239461], "h2h": [{"away": "Gil Vicente", "away_goals": 0.0, "away_xg": null, "date": "2026-03-21T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 0.0, "away_xg": null, "date": "2025-11-03T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": null, "date": "2025-03-15T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": null, "date": "2024-10-25T00:00:00+00:00", "home": "Santa Clara", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 2.0, "away_xg": null, "date": "2023-05-06T00:00:00+00:00", "home": "Santa Clara", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 0.0, "away_xg": null, "date": "2022-12-29T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.1920966677518885, "-10": 1.1996155918217067e-08, "-11": 9.555371159203336e-10, "-12": 6.968650568088801e-11, "-13": 4.405176246092179e-12, "-2": 0.07378397012914953, "-3": 0.020162798489601407, "-4": 0.004250653685827311, "-5": 0.0007275048612845107, "-6": 0.00010465786696863113, "-7": 1.2975748177646394e-05, "-8": 1.4128567927799723e-06, "-9": 1.3710000623006802e-07, "0": 0.30876315458610415, "1": 0.2372108917763948, "10": 9.889857876941964e-08, "11": 9.72770304788671e-09, "12": 8.760446194525804e-10, "13": 6.838417661478103e-11, "2": 0.11251012561452466, "3": 0.037966030680987514, "4": 0.009883594125263434, "5": 0.0020888625996198945, "6": 0.000371074104798356, "7": 5.6811462916991024e-05, "8": 7.638648095426533e-06, "9": 9.153151029980171e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:18.664785+00:00", "p_over_1_5": 0.5864884048091846, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Vitória SC vs FC Porto

The model's most likely 1X2 outcome is **FC Porto win** at **59.6%**. Expected goals are 0.69 for Vitória SC and 1.65 for FC Porto (2.34 combined). The most likely exact score is 0-1 at 11.9%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 50.7%; Under 3.5 goals: 70.8%; Double Chance 1X: 40.4%; Double Chance X2: 82.5%; Double Chance 12 (either team wins): 77.1%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 48.1%; BTTS No (at least one team does not score): 51.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Vitória SC win | 17.5% | 5.71 |
| Draw | 22.9% | 4.37 |
| FC Porto win | 59.6% | 1.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Vitória SC expected goals | 0.69 |
| FC Porto expected goals | 1.65 |
| Expected total goals | 2.34 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 75.0% |
| Under 1.5 | 25.0% |
| Over 2.5 | 50.7% |
| Under 2.5 | 49.3% |
| Over 3.5 | 29.2% |
| Under 3.5 | 70.8% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 11.90% |
| 2 | 0-2 | 11.10% |
| 3 | 1-1 | 10.84% |
| 4 | 1-2 | 9.02% |
| 5 | 0-3 | 7.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Vitória SC win | 17.5% | 18.2% | 5.04 | -11.8% |
| Draw | 22.9% | 22.8% | 4.07 | -6.9% |
| FC Porto win | 59.6% | 59.0% | 1.65 | -1.6% |
| Over 2.5 | 50.7% | 50.7% | 1.89 | -4.2% |
| Under 2.5 | 49.3% | 49.3% | 1.94 | -4.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T18:00:00+00:00 |
| Fixture id | c468a7bc1110c030b62f381e3a480145 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T12:16:29Z |
| Market best draw last update utc | 2026-11-06T12:16:29Z |
| Market best away last update utc | 2026-11-06T12:16:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Guimaraes |
| Matched away-team name | Porto |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6913 |
| Dc lambda away | 1.6519 |
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
| P btts yes | 48.1% |
| P btts no | 51.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.03 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.00 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.42 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.15 |
| Fair Under 4.5 odds | 1.16 |
| Score matrix json | [[0.06654889704784128,0.11898181699510776,0.11103487746042867,0.07188648384968063,0.03490569818104282,0.013559241740673545,0.004389279452990901,0.001217879361329311,0.0002956809620593994,6.381017445416715e-05,1.2393643817852337e-05,2.1883430516970673e-06,3.5419566140253183e-07,5.2918675247467615e-08,7.341587964838174e-09,9.506219248153532e-10,1.1539763880117097e-10],[0.0642950193034704,0.10835759200565095,0.09024780277041444,0.05842846288218451,0.028370928460105176,0.011020787362644537,0.003567553145802572,0.0009898775854332504,0.00024032590261031353,5.186413648214048e-05,1.0073403496832981e-05,1.7786587119344345e-06,2.878859410979601e-07,4.301165792079249e-08,5.9671537252652185e-09,7.726539799221439e-10,9.379380231595383e-11],[0.02381623144479743,0.04625749610234432,0.04501549674710908,0.023744973268643048,0.011529773412834213,0.0044787812038297745,0.0014498319809021529,0.0004022802525669091,9.766699056846819e-05,2.107727079613423e-05,4.093770141426861e-06,7.228361227657746e-07,1.1699510202027814e-07,1.7479677150306236e-08,2.42501511604046e-09,3.1400189555142415e-10,3.8117232918612186e-11],[0.0064525147633022655,0.012532510746110297,0.01217074515618683,0.007895976294322248,0.0031237533669540426,0.0012134330280715038,0.00039280195453099236,0.00010898950468672784,2.646084876992613e-05,5.710450089360581e-06,1.1091222528782198e-06,1.9583748018258312e-07,3.169740035360663e-08,4.7357565839723304e-09,6.570076325362697e-10,8.50723117738703e-11,1.0327074991425799e-11],[0.0013111314504292198,0.002546568213298893,0.002473058541483901,0.0016011138749178646,0.0007790622331638009,0.00024656591491158174,7.981616707097284e-05,2.214633714194536e-05,5.376764300426952e-06,1.160346156950943e-06,2.2537028142734723e-07,3.979358263549091e-08,6.440815716815291e-09,9.622913897287433e-10,1.3350196036583546e-10,1.7286436005046345e-11,2.0984303498547686e-12],[0.00021313435066669696,0.0004139639563921898,0.00040201440231438826,0.00026027319073334984,0.00012638005023799288,4.919471410904603e-05,1.2974722660956219e-05,3.6000548875927448e-06,8.740337724979616e-07,1.8862305883164933e-07,3.663564669725804e-08,6.468748341701654e-09,1.0470033917025544e-09,1.5642775591634776e-10,2.1701755095561645e-11,2.81004113818705e-12,3.411157515054437e-13],[2.8872169541838302e-05,5.6077481155800436e-05,5.4458739032794745e-05,3.5257815863760195e-05,1.712002887269697e-05,6.650335681246469e-06,2.1572587468777258e-06,4.876801639405683e-07,1.1840067631480476e-07,2.555175604989174e-08,4.962834941479005e-09,8.762867095842499e-10,1.4183194469383737e-10,2.11904307106691e-11,2.9398205897573046e-12,3.8066123038117093e-13,4.6209124808128176e-14],[3.352421357481517e-06,6.511299583082976e-06,6.323343300214953e-06,4.093875063615831e-06,1.9878502843494758e-06,7.721874637763209e-07,2.499657896387794e-07,6.950122459520526e-08,1.3747804973326396e-08,2.9668796651628632e-09,5.762474422769143e-10,1.0174788826418065e-10,1.6468469398385354e-11,2.460475039318997e-12,3.413500782469703e-13,4.419954783258652e-14,5.365459519514673e-15],[3.406009314293398e-07,6.615381738528255e-07,6.424421002432306e-07,4.1593150476478774e-07,2.019625775502602e-07,7.845307655415284e-08,2.53961455610098e-08,7.0465874563974705e-09,1.7143471947760917e-09,3.0143047953625564e-10,5.854586719395514e-11,1.0337431312567153e-11,1.6731715432452331e-12,2.499805366889392e-13,3.4680650848060076e-14,4.4906071031131184e-15,5.451225591958395e-16],[3.075958992555623e-08,5.974335672665567e-08,5.801879481499445e-08,3.756267626748575e-08,1.8239192828053484e-08,7.085078872441792e-09,2.2935199262907973e-09,6.363756541233091e-10,1.5450148152357157e-10,3.341181442035343e-11,5.287263482119204e-12,9.335709879705258e-13,1.5110372813531324e-13,2.2575683412414378e-14,3.132001412800099e-15,4.0554567020379817e-16,4.922988997612994e-17],[2.500102191664732e-09,4.855867631890051e-09,4.7156973297033e-09,3.0530488048902615e-09,1.4824594890234906e-09,5.758666243593917e-10,1.864145200967815e-10,5.172384194478148e-11,1.2557693178204637e-11,2.710044592868199e-12,5.274561480148771e-13,7.587951850946253e-14,1.2281527900537423e-14,1.8349241883362232e-15,2.545652791662492e-16,3.296226059419172e-17,4.001345795656293e-18],[1.8473206933613432e-10,3.587991239126505e-10,3.4844196728570957e-10,2.2558918807076612e-10,1.0953864607108127e-10,4.2550673942127645e-11,1.3774132980080547e-11,3.821864717502705e-12,9.278855298924076e-13,2.0024467291890588e-13,3.889287521634708e-14,6.8815661157966724e-15,9.074797307245415e-16,1.3558219480643274e-16,1.8809779439535103e-17,2.4355750856357484e-18,2.9565867004373753e-19],[1.251233226601822e-11,2.4302298303076386e-11,2.3600784020725803e-11,1.5279679846094695e-11,7.419307002495904e-12,2.882056009117435e-12,9.329540298143344e-13,2.5886377710711783e-13,6.284784280589024e-14,1.3563036948947338e-14,2.634304802823594e-15,4.651386384855934e-16,7.544163516538264e-17,9.183297068400588e-18,1.2740300644266367e-18,1.6496715940998392e-19,2.002564866084504e-20],[7.822978483937945e-13,1.5194318108985815e-12,1.4755716334326405e-12,9.553183542135723e-13,4.638709859383065e-13,1.8019232281788353e-13,5.833028684478278e-14,1.618471852829345e-14,3.929381921607592e-15,8.479901586104175e-16,1.6470238604989869e-16,2.9081465258106886e-17,4.706999121395442e-18,7.047104095102829e-19,7.965509203242523e-20,1.0314100610368059e-20,1.2520465031619973e-21],[4.541730075162554e-14,8.82125544239389e-14,8.566619580224477e-14,5.546222720150577e-14,2.6930622551972047e-14,1.0461295445662802e-14,3.386439303134226e-15,9.39624505537296e-16,2.281252861273597e-16,4.923115172450406e-17,9.562007382606422e-18,1.6883616088645078e-18,2.732708458459692e-19,4.082808662494886e-20,5.675980746032535e-21,5.987982842665409e-22,7.268915887456836e-23],[2.4609754426384656e-15,4.779873012641619e-15,4.641896384078643e-15,3.0052684082520175e-15,1.459258909238387e-15,5.6685427720053e-16,1.8349712169322986e-16,5.0914360720695935e-17,1.2361164527907624e-17,2.6676322326900182e-18,5.181255812539649e-19,9.148532363100449e-20,1.4807415449318662e-20,2.212304934267125e-21,3.069205947430604e-22,3.9823982989218443e-23,3.9387244943207265e-24],[1.2501568845407502e-16,2.428139285932042e-16,2.358048203707023e-16,1.5266535884003208e-16,7.412924729374466e-17,2.879576792582079e-17,9.32151479464818e-18,2.5864109602299646e-18,6.279377952238607e-19,1.3551369685935408e-19,2.6320387080614987e-20,4.647385146156483e-21,7.522054891524681e-22,1.1238341498086301e-22,1.559133374016957e-23,2.0188362192899582e-24,2.455788869908893e-25]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.23635838877345527, "-10": 1.4294169746601655e-05, "-11": 2.4943833051296262e-06, "-12": 3.9971950518148855e-07, "-13": 5.921015794327569e-08, "-14": 8.15235917767893e-09, "-15": 1.044415727131307e-09, "-16": 1.1539763880117097e-10, "-2": 0.18229008443252526, "-3": 0.10515204197755489, "-4": 0.04749087748291433, "-5": 0.017556733862624924, "-6": 0.0054827664624392605, "-7": 0.0014804325191109845, "-8": 0.0003518413063911873, "-9": 7.463909585329104e-05, "0": 0.22864844755046132, "1": 0.12445766199246665, "10": 2.8834849247506662e-09, "11": 2.1056688955452201e-10, "12": 1.4120509670374592e-11, "13": 8.753049645606521e-13, "14": 5.043297858463786e-14, "15": 2.7037893712316696e-15, "16": 1.2501568845407502e-16, "2": 0.03909999218474327, "3": 0.009438423844325595, "4": 0.0017838572588743334, "5": 0.0002759699357239054, "6": 3.606499986096453e-05, "7": 4.075143854938715e-06, "8": 4.0529317761107644e-07, "9": 3.5979653722943e-08} |
| Raw goal margin distribution | {"-1": 0.273640584946539, "-10": 4.439454974995867e-06, "-11": 6.610065578535164e-07, "-12": 9.033556936863438e-08, "-13": 1.1406883404948646e-08, "-14": 1.3353278062868466e-09, "-15": 1.3665188227431853e-10, "-2": 0.1885660280707427, "-3": 0.0952403968483758, "-4": 0.03727941282231511, "-5": 0.011876033190605243, "-6": 0.0031847775775250236, "-7": 0.0007367683200119442, "-8": 0.00014978696016453545, "-9": 2.7151515306091415e-05, "0": 0.2302784505313713, "1": 0.11769958881797093, "10": 7.311577078477404e-10, "11": 4.555702081379367e-11, "12": 2.6054123925618587e-12, "13": 1.3767428556834423e-13, "14": 6.744377368312996e-15, "15": 2.8882695959398163e-16, "2": 0.03302172334963889, "3": 0.00697952100234353, "4": 0.0011432510951213115, "5": 0.00015240952380226165, "6": 1.7103616537248557e-05, "7": 1.65580019122008e-06, "8": 1.4087020048354078e-07, "9": 1.0685807308415627e-08} |
| Research history json | {"away": [{"away": "Estoril", "away_goals": 0.0, "away_xg": 0.63, "date": "2026-10-31T00:00:00+00:00", "home": "Porto", "home_goals": 4.0, "home_xg": 3.1, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 1.0, "away_xg": 1.08, "date": "2026-10-24T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": 0.35, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 2.0, "away_xg": 2.13, "date": "2026-10-10T00:00:00+00:00", "home": "Maritimo", "home_goals": 1.0, "home_xg": 0.19, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 1.0, "away_xg": 0.84, "date": "2026-09-20T00:00:00+00:00", "home": "Porto", "home_goals": 3.0, "home_xg": 1.3, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 4.0, "away_xg": 2.6, "date": "2026-09-12T00:00:00+00:00", "home": "Casa Pia", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.85, "date": "2026-09-04T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.9, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 3.0, "away_xg": 1.47, "date": "2026-08-29T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 0.0, "home_xg": 0.8, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": 0.54, "date": "2026-08-23T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.99, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 2.0, "away_xg": 1.98, "date": "2026-08-15T00:00:00+00:00", "home": "Rio Ave", "home_goals": 0.0, "home_xg": 0.57, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 0.0, "away_xg": 1.66, "date": "2026-08-09T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.59, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 15.9% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 61.1% |
| Raw p over 1 5 | 67.3% |
| Raw p under 3 5 | 79.1% |
| Raw p btts yes | 39.8% |
| P home draw | 40.4% |
| P draw away | 82.5% |
| P home away | 77.1% |
| Raw p home draw | 38.9% |
| Raw p draw away | 84.1% |
| Raw p home away | 77.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1758 |
| Totals anchor target over 2 5 | 0.5070 |
| Totals anchor reference over odds | 1.89 |
| Totals anchor reference under odds | 1.94 |
| Totals anchor reference last update utc | 2026-11-06T12:16:29Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4142 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.65, "draw": 4.07, "home": 5.04}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T12:16:29Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.89, "under": 1.94}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.04 |
| Reference draw odds | 4.07 |
| Reference away odds | 1.65 |
| Market reference 1x2 last update utc | 2026-11-06T12:16:29Z |
| Market reference home last update utc | 2026-11-06T12:16:29Z |
| Market reference draw last update utc | 2026-11-06T12:16:29Z |
| Market reference away last update utc | 2026-11-06T12:16:29Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.94 |
| Market reference over 2 5 last update utc | 2026-11-06T12:16:29Z |
| Market reference under 2 5 last update utc | 2026-11-06T12:16:29Z |
| Market best over 2 5 last update utc | 2026-11-06T12:16:29Z |
| Market best under 2 5 last update utc | 2026-11-06T12:16:29Z |
| Home probability edge | -0.7% |
| Draw probability edge | +0.1% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0230 |
| Raw ev home | -0.1986 |
| Raw edge prob draw | 0.0023 |
| Raw ev draw | -0.0628 |
| Raw edge prob away | 0.0206 |
| Raw ev away | 0.0077 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,465.5432 |
| Elo away rating | 1,690.2042 |
| Elo rating diff | -164.6610 |
| Elo home expectancy | 0.2793 |
| Research p home | 0.1535 |
| Research p draw | 0.2412 |
| Research p away | 0.6052 |
| Research p over 1 5 | 0.6790 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [0.6912751038993512, 1.6518962811282238], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:18.484557+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T12:17:18.065934+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:18.689209+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Vit%C3%B3ria+SC%22+%22FC+Porto%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:18.771384+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Vit%C3%B3ria+SC_vs_FC+Porto&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 0.430110668809516, "goals_for": 2.5822078216963384, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 3.0, "results": "WWWWWWWWWW", "xg_against": 0.7229623216576558, "xg_for": 2.179102135361633, "xg_matches": 10}, "venue": {"goals_against": 0.421593215819354, "goals_for": 2.304327993843115, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 3.0, "results": "WWWWW", "xg_against": 0.6668151416998931, "xg_for": 1.8153351910568654, "xg_matches": 5}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [0.6912751038993512, 1.6518962811282238], "h2h": [], "margin_distribution": {"-1": 0.2681581019516065, "-10": 4.439454974995867e-06, "-11": 6.610065578535164e-07, "-12": 9.033556936863438e-08, "-13": 1.1406883404948646e-08, "-14": 1.3353278062868466e-09, "-15": 1.3665188227431853e-10, "-2": 0.1885660280707427, "-3": 0.0952403968483758, "-4": 0.03727941282231511, "-5": 0.011876033190605243, "-6": 0.0031847775775250236, "-7": 0.0007367683200119442, "-8": 0.00014978696016453545, "-9": 2.7151515306091415e-05, "0": 0.24124341652123618, "1": 0.11221710582303848, "10": 7.311577078477404e-10, "11": 4.555702081379367e-11, "12": 2.6054123925618587e-12, "13": 1.3767428556834423e-13, "14": 6.744377368312996e-15, "15": 2.8882695959398163e-16, "2": 0.03302172334963889, "3": 0.00697952100234353, "4": 0.0011432510951213115, "5": 0.00015240952380226165, "6": 1.7103616537248557e-05, "7": 1.65580019122008e-06, "8": 1.4087020048354078e-07, "9": 1.0685807308415627e-08}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:18.771795+00:00", "p_over_1_5": 0.6789798907058394, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
