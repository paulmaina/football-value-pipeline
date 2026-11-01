# Primeira Liga — football model report

Fixtures in this report: **8**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,611 |
| Training data through | 2026-10-26 |
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
| Training sha256 | 84c0a9d8af08458f9d90e4a3ffe4465c5e09f0dc593fdcb0fb4ebd37c58b23a7 |
| Training as of utc | 2026-10-31T12:02:52.604255+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-31', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1611, 'tune_start_date': '2025-11-01', 'audit_start_date': '2026-05-02', 'training_shot_matches': 1306, 'tuning_matches': 197, 'audit_matches': 102, 'audit_matchdays': 41, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8837369848433605, 'audit_candidate_poisson_score': 0.8736504139029021, 'audit_gain': 0.010086570940458395, 'audit_gain_lower95': 0.00023341876008991057, 'audit_baseline_briers': [0.5954781285766396, 0.18598260384228765, 0.24306091556742074, 0.2491479077062837], 'audit_candidate_briers': [0.5923611513039804, 0.1851266567366948, 0.24107651149451814, 0.24810660644395263], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1458.628 |
| Base scoring parameter | 0.094 |
| Home-advantage parameter | 0.170 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1611, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 5, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 8.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 47.00 |
| Over 1 5 in window quote fixtures | 6 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 6.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 6.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 4, 'ANCHORED_MAIN': 2, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
| Shot features applied fixtures | 8 |
| Goal rate features used | {'shot_features': 8} |
| Legacy comparison status | {'AVAILABLE': 8} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-31 — FC Porto vs Estoril

The model's most likely 1X2 outcome is **FC Porto win** at **81.6%**. Expected goals are 2.34 for FC Porto and 0.69 for Estoril (3.04 combined). The most likely exact score is 2-0 at 12.5%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 66.2%; Under 3.5 goals: 55.9%; Double Chance 1X: 94.0%; Double Chance X2: 18.4%; Double Chance 12 (either team wins): 87.6%; Under 4.5 goals: 74.6%; BTTS Yes (both teams score): 48.2%; BTTS No (at least one team does not score): 51.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Porto win | 81.6% | 1.23 |
| Draw | 12.4% | 8.05 |
| Estoril win | 6.0% | 16.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Porto expected goals | 2.34 |
| Estoril expected goals | 0.69 |
| Expected total goals | 3.04 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 66.2% |
| Under 2.5 | 33.8% |
| Over 3.5 | 44.1% |
| Under 3.5 | 55.9% |
| Over 4.5 | 25.4% |
| Under 4.5 | 74.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.46% |
| 2 | 3-0 | 10.74% |
| 3 | 1-0 | 10.00% |
| 4 | 2-1 | 9.51% |
| 5 | 3-1 | 8.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Porto win | 81.6% | 84.5% | 1.17 | -4.5% |
| Draw | 12.4% | 11.1% | 7.80 | -3.1% |
| Estoril win | 6.0% | 4.4% | 18.33 | +9.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T20:30:00+00:00 |
| Fixture id | 60352ce6c1b34bca7b294edae8aa388b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:35Z |
| Market best draw last update utc | 2026-10-31T12:02:35Z |
| Market best away last update utc | 2026-10-31T12:02:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Porto |
| Matched away-team name | Estoril |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5378 |
| Dc lambda away | 0.6307 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.8904 |
| Shot lambda away | 0.8335 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 48.2% |
| P btts no | 51.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.64 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.76 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.96 |
| Fair Over 3.5 odds | 2.27 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.93 |
| Fair Under 4.5 odds | 1.34 |
| Goal margin distribution | {"-1": 0.04412103751969939, "-10": 5.098586390036018e-10, "-11": 3.485410427654117e-11, "-12": 2.1889370350104106e-12, "-13": 1.271193015418283e-13, "-14": 6.864615277518063e-15, "-15": 3.4638047316764433e-16, "-16": 1.6398012277651914e-17, "-17": 7.27644001088745e-19, "-18": 2.7799279156741354e-20, "-2": 0.012414175754400066, "-3": 0.0027446364963810105, "-4": 0.00047911334814051596, "-5": 6.879098027734855e-05, "-6": 8.368553814769938e-06, "-7": 8.819853317468675e-07, "-8": 8.192862597608073e-08, "-9": 6.799829888055031e-09, "0": 0.12424650790684347, "1": 0.23206232236196697, "10": 0.00016402925414618687, "11": 3.7998604300924836e-05, "12": 8.087032331311889e-06, "13": 1.591510833854427e-06, "14": 2.912436700443016e-07, "15": 4.980075018356731e-08, "16": 7.989431585519398e-09, "17": 1.2013949978535925e-09, "18": 1.5554017813878713e-10, "2": 0.22964229996793933, "3": 0.17205251423376433, "4": 0.1017786418123316, "5": 0.04952130377021698, "6": 0.020415178251802654, "7": 0.007291322648847092, "8": 0.0022952120576434183, "9": 0.0006455462827081772} |
| Raw goal margin distribution | {"-1": 0.07242031304793772, "-10": 3.837321728445025e-10, "-11": 2.383536530053711e-11, "-12": 1.3596384536093648e-12, "-13": 7.169541988887269e-14, "-14": 3.5146258394598674e-15, "-15": 1.6095828024527413e-16, "-16": 6.9153036789475045e-18, "-17": 2.7886322052210954e-19, "-18": 9.82898845182115e-21, "-2": 0.01910832188943476, "-3": 0.003914051718461195, "-4": 0.0006283088545142137, "-5": 8.260208810753336e-05, "-6": 9.176419605779766e-06, "-7": 8.816200490281813e-07, "-8": 7.456296176674e-08, "-9": 5.629530285421735e-09, "0": 0.15605006284852882, "1": 0.23611082004996659, "10": 7.663905212846492e-05, "11": 1.6131914644224774e-05, "12": 3.1183850034978737e-06, "13": 5.572369392357865e-07, "14": 9.256989568851762e-08, "15": 1.436634167658241e-08, "16": 2.0916369996160016e-09, "17": 2.858304472854919e-10, "18": 3.414037336340665e-11, "2": 0.21943552144058248, "3": 0.15231866809802647, "4": 0.08285943066227912, "5": 0.03691492428640658, "6": 0.013897171316581405, "7": 0.004524564631649294, "8": 0.0012967632080512707, "9": 0.000331781281762499} |
| Unadjusted home-win probability | 74.8% |
| Unadjusted draw probability | 15.6% |
| Unadjusted away-win probability | 9.6% |
| Raw p over 1 5 | 80.2% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 44.7% |
| P home draw | 94.0% |
| P draw away | 18.4% |
| P home away | 87.6% |
| Raw p home draw | 90.4% |
| Raw p draw away | 25.2% |
| Raw p home away | 84.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1034 |
| Totals anchor target over 2 5 | 0.6623 |
| Totals anchor reference over odds | 1.46 |
| Totals anchor reference under odds | 2.71 |
| Totals anchor reference last update utc | 2026-10-31T12:02:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6044 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 4.48, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.48, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.17 |
| Reference draw odds | 7.80 |
| Reference away odds | 18.33 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:35Z |
| Market reference home last update utc | 2026-10-31T12:02:35Z |
| Market reference draw last update utc | 2026-10-31T12:02:35Z |
| Market reference away last update utc | 2026-10-31T12:02:35Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.68 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:38Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:38Z |
| Home probability edge | -2.9% |
| Draw probability edge | +1.4% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | -0.0973 |
| Raw ev home | -0.1251 |
| Raw edge prob draw | 0.0454 |
| Raw ev draw | 0.2172 |
| Raw edge prob away | 0.0519 |
| Raw ev away | 0.7627 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.03461697334854927, 0.02355604673197406, 0.00661959002339472, 0.001398546966876545, 0.000221607412050481, 2.8091924684026325e-05, 2.9675460203516746e-06, 2.6869936514162956e-07, 2.1288441625107063e-08, 1.4992310882849042e-09, 9.502454459072085e-11, 5.475330378735358e-12, 2.891986764574713e-13, 1.4100034211561821e-14, 6.383507138792264e-16, 2.6973376041238112e-17, 1.0685197208845138e-18, 3.983830372494475e-20, 1.4027993335720107e-21], [0.11229109456405174, 0.05794289441052596, 0.0169115744790771, 0.0035729752309782495, 0.0005661574569969049, 7.176859516609481e-05, 7.581417484451613e-06, 6.864668823920666e-07, 5.438721504112936e-08, 3.830200680294626e-09, 2.427664942250055e-10, 1.39882465787587e-11, 7.388380456910682e-13, 3.602243913650664e-14, 1.6308435421812296e-15, 6.891095313477115e-17, 2.7298293063826513e-18, 1.0177797086880465e-19, 3.583839078411181e-21], [0.1390332222369802, 0.08812229635101373, 0.024690890675490754, 0.004564076968289257, 0.0007232029451257394, 9.167636803190673e-05, 9.684414441993572e-06, 8.768848046453288e-07, 6.94735953908785e-08, 4.892653762973976e-09, 3.101070937626714e-10, 1.7868423347391584e-11, 9.437831190089704e-13, 4.60146444282844e-14, 2.0832205566996638e-15, 8.80260493659112e-17, 3.487052178979391e-18, 1.3000999522583984e-19, 4.5779543205378126e-21], [0.11839961309874641, 0.07504426370518186, 0.02378234762623774, 0.00444236679827283, 0.0006158740156997263, 7.807088356748856e-05, 8.247172183534197e-06, 7.467482946285472e-07, 5.916317468955993e-08, 4.166545975427769e-09, 2.6408479448238717e-10, 1.5216610655903055e-11, 8.037183799806128e-13, 3.918571410147586e-14, 1.7740544593879839e-15, 7.496230051958701e-17, 2.9695465745775255e-18, 1.1071550300022482e-19, 3.8985503724536594e-21], [0.07562114376180472, 0.04793033444640899, 0.015189647007858182, 0.0032091768033500044, 0.00044958788462690975, 4.986341893654953e-05, 5.2674208723913445e-06, 4.769437894606242e-07, 3.7787175325248984e-08, 2.6611486638492083e-09, 1.686694211762648e-10, 9.718760660288324e-12, 5.133302513905109e-13, 2.502768752297602e-14, 1.1330782576355385e-15, 4.787798503682203e-17, 1.8966321134530757e-18, 7.071334736590595e-20, 2.4899814320514612e-21], [0.03863902750475516, 0.024490260512593873, 0.0077612313081754335, 0.0016397460366751769, 0.00025982672317339194, 2.9120227148376733e-05, 2.691416842471113e-06, 2.436969778880716e-07, 1.93075591572414e-08, 1.3597281302778603e-09, 8.618254207538968e-11, 4.9658526938954485e-12, 2.622888350509058e-13, 1.2788030681296445e-14, 5.789523906134421e-16, 2.446351230202383e-17, 9.690943134759901e-19, 3.61313627102873e-20, 1.2722693185177759e-21], [0.016452347983696554, 0.010427857898726646, 0.003304702175756061, 0.00069819749984513, 0.00011063321054304897, 1.4024349589080515e-05, 1.3098224355523422e-06, 1.0376522758747847e-07, 8.22108377162572e-09, 5.78966961831515e-10, 3.669619200869857e-11, 2.1144408084724795e-12, 1.1168156822696492e-13, 5.445093843756418e-15, 2.465156814620436e-16, 1.0416468614454791e-17, 4.1263659838142536e-19, 1.5384594044496795e-20, 5.417273391432773e-22], [0.006004582228088998, 0.003805835512218665, 0.001206110882977655, 0.00025481981680795226, 4.037759294427241e-05, 5.118440260718308e-06, 5.406965594898988e-07, 4.328490937121385e-08, 3.000433346027696e-09, 2.113044735687081e-10, 1.3392939572656987e-11, 7.717034500778496e-13, 4.076021005909154e-14, 1.98728556902007e-15, 8.997036054179392e-17, 3.80167878674719e-18, 1.505991964037893e-19, 5.614886098780021e-21, 1.9771319913200662e-22], [0.00191754586022673, 0.0012153824952250468, 0.000385168000499556, 8.137596693039746e-05, 1.2894466801373276e-05, 1.634559001764534e-06, 1.7266987275793605e-07, 1.563456299277377e-08, 1.095157813625251e-09, 6.747946870369e-11, 4.276996276889775e-12, 2.4644125099947467e-13, 1.3016654463512565e-14, 6.346338631414734e-16, 2.8731772810600647e-17, 1.2140550570424802e-18, 4.8093415103329354e-20, 1.7930975354111947e-21, 6.313913476515441e-23], [0.0005443223911931092, 0.00034500343367898506, 0.00010933536005141351, 2.3099713975011745e-05, 3.6602759537932347e-06, 4.639925870046684e-07, 4.9014774549119006e-08, 4.4380908378794455e-09, 3.5161987702992633e-10, 2.189333158468659e-11, 1.2140856126827643e-12, 6.995581895329177e-14, 3.694960642076044e-15, 1.8014975760550613e-16, 8.155918251485316e-18, 3.4462662166072625e-19, 1.3651993025393253e-20, 5.089959819798456e-22, 1.7922932392954166e-23], [0.00013906221724847568, 8.814067402330381e-05, 2.793274323895286e-05, 5.901461147188241e-06, 9.351187790751499e-07, 1.1853974589267692e-07, 1.252218048901923e-08, 1.1338331148069699e-09, 8.983102756665897e-11, 6.326318834990632e-12, 3.5451288312065176e-13, 1.787214975991391e-14, 9.439799424871623e-16, 4.602424066091637e-17, 2.0836550068477456e-18, 8.804440696614659e-20, 3.487779394506644e-21, 1.3003710846716053e-22, 4.578909040827066e-24], [3.22975377342333e-05, 2.0470885633168746e-05, 6.487447465106622e-06, 1.3706286859201739e-06, 2.1718360781782283e-07, 2.7531143913334414e-08, 2.9083068346043627e-09, 2.633354949631568e-10, 2.086347434943493e-11, 1.4693029158798378e-12, 9.312763158281529e-14, 4.744241841360093e-15, 2.1924163454378331e-16, 1.0689241685103901e-17, 4.839339364807005e-19, 2.0448527375313962e-20, 8.100452360937346e-22, 3.020143429803354e-23, 1.063462746775348e-24], [6.876083122883774e-06, 4.358211835557964e-06, 1.3811649789678222e-06, 2.9180418806374373e-07, 4.623796874460377e-08, 5.8613271257366035e-09, 6.191728826558274e-10, 5.606361597816681e-11, 4.441793211586245e-12, 3.1281174018342253e-13, 1.9826692086251554e-14, 1.1424173612959963e-15, 5.3348780315455287e-17, 2.27571881646765e-18, 1.0302859619229251e-19, 4.353451805838133e-21, 1.724570591885324e-22, 6.429826767985395e-24, 2.2640915555512637e-25], [1.3512966983198263e-06, 8.564813948173984e-07, 2.7142831791879974e-07, 5.734573431408177e-08, 9.086745082190671e-09, 1.1518755447299713e-09, 1.216806511889707e-10, 1.1017693912838408e-11, 8.729069143245965e-13, 6.147416547347679e-14, 3.896367026976735e-15, 2.2450932905172524e-16, 1.1858243489064174e-17, 5.111612902937914e-19, 2.024731222399517e-20, 8.555459476552043e-22, 3.389148306073347e-23, 1.2635978255456533e-24, 4.449421842397842e-26], [2.4659009606553067e-07, 1.5629419481965975e-07, 4.9531339100971285e-08, 1.0464681924436213e-08, 1.6581860560500342e-09, 2.1019891603647794e-10, 2.2204778198091133e-11, 2.010553421587957e-12, 1.592915901646217e-13, 1.1218054768061854e-14, 7.110248405723215e-16, 4.0969371927947745e-17, 2.1639403136058753e-18, 1.0550405287939693e-19, 4.223009456069731e-21, 1.561234906316924e-22, 6.1846551346871974e-24, 2.305864504641531e-25, 8.119485239009085e-27], [4.199884243260516e-08, 2.6619784679500557e-08, 8.436100798731207e-09, 1.7823283832734736e-09, 2.8241967541746373e-10, 3.58007531323334e-11, 3.78188335895188e-12, 3.424343382110846e-13, 2.71302964024362e-14, 1.910641676699616e-15, 1.2110064727388458e-16, 6.977839838739557e-18, 3.6855895558977933e-19, 1.7969286534952708e-20, 8.135233372754244e-22, 3.0392029583701534e-23, 1.0533608634172503e-24, 3.927312635282841e-26, 1.3828981237607523e-27], [6.706104053685971e-09, 4.250475384742009e-09, 1.3470221198228774e-09, 2.845906911660661e-10, 4.509495072862775e-11, 5.7164331633903916e-12, 6.038667223919854e-13, 5.467770468397129e-14, 4.331990601265574e-15, 3.0507892958758097e-16, 1.9336569642141387e-17, 1.1141764229248115e-18, 5.884911495046593e-20, 2.869219680691478e-21, 1.2989815513666429e-22, 5.488819405044538e-24, 1.9223829478926768e-25, 6.270879304786767e-27, 2.2081224568196875e-28], [1.007799912323864e-09, 6.387656209603947e-10, 2.0243180889948217e-10, 4.276856894991148e-11, 6.776913544247872e-12, 8.590711976357651e-13, 9.074968491540798e-14, 8.217019232841862e-15, 6.510158078659134e-16, 4.58475615691095e-17, 2.9059187024220487e-18, 1.6743952857691856e-19, 8.843902870075243e-21, 4.311891553560709e-22, 1.9521222502625397e-23, 8.248651781841919e-25, 3.267609915100085e-26, 1.0771153876281715e-27, 3.318388143947883e-29], [1.4303909739490426e-10, 9.066130761847938e-11, 2.8731559583321886e-11, 6.07023023584183e-12, 9.618611637475564e-13, 1.2192972752342392e-13, 1.2880287902823764e-14, 1.1662583018409308e-15, 9.240000163547307e-17, 6.5072379392063915e-18, 4.1244296929830035e-19, 2.3765033855424734e-20, 1.2552331752706492e-21, 6.119955641431253e-23, 2.7706869316766765e-24, 1.1707479740486162e-25, 4.637785409375534e-27, 1.7291351777473542e-28, 5.3831612309486966e-30]] |
| Legacy trial inputs | {"lambda_home": 2.5547767186953894, "lambda_away": 0.6338218659768275, "rho": 0.05, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8187 |
| Legacy p draw | 0.1222 |
| Legacy p away | 0.0591 |
| Legacy p over 1 5 | 0.8295 |
| Legacy p under 3 5 | 0.5989 |
| Legacy p btts yes | 0.4245 |
| Legacy p over 2 5 | 0.6259 |
| Legacy goal margin distribution | {"-1": 0.04570023386519174, "-10": 1.0999691796267456e-10, "-11": 6.262005985975756e-12, "-12": 3.2738123175640066e-13, "-13": 1.582194533530022e-14, "-14": 7.108619246774092e-16, "-15": 2.9837113893219057e-17, "-16": 1.1748756460738563e-18, "-17": 4.342214280335593e-20, "-18": 1.4027993335720107e-21, "-2": 0.010999358637652628, "-3": 0.002065124808047593, "-4": 0.00030384635433774776, "-5": 3.661213963486265e-05, "-6": 3.7278267930818516e-06, "-7": 3.2825330532600267e-07, "-8": 2.54444923784683e-08, "-9": 1.7606953414460745e-09, "0": 0.1221731875693695, "1": 0.22767932310657862, "10": 0.00016097330819391165, "11": 3.6937930797659024e-05, "12": 7.783924152087633e-06, "13": 1.5163184834726552e-06, "14": 2.746006332949677e-07, "15": 4.645781985648249e-08, "16": 7.373601234229688e-09, "17": 1.0984612199423434e-09, "18": 1.4303909739490426e-10, "2": 0.23102280783678317, "3": 0.17483143867490988, "4": 0.10368429751637095, "5": 0.05035815403434424, "6": 0.020667414490664573, "7": 0.007335424713166233, "8": 0.002291900078226468, "9": 0.0006392516176508002} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7923 |
| Legacy raw p draw | 0.1337 |
| Legacy raw p away | 0.0739 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.5548 |
| Legacy lambda away | 0.6338 |
| Legacy model home team | Porto |
| Legacy model away team | Estoril |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 93.4% |
| Market reference home draw last update utc | 2026-10-31T12:02:12Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 19.2% |
| Market reference draw away last update utc | 2026-10-31T12:02:12Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 87.4% |
| Market reference home away last update utc | 2026-10-31T12:02:12Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 5.00 |
| Market reference dc home draw odds | 1.03 |
| Market reference dc home away odds | 1.10 |
| Market p over 1 5 | 85.5% |
| Market over 1 5 odds | 1.15 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.56 |
| Market reference over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 57.1% |
| Market under 3 5 odds | 1.69 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 3 5 odds | 1.69 |
| Market reference under 3 5 opposite odds | 2.21 |
| Market reference under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 41.5% |
| Market reference btts yes odds | 2.36 |
| Market reference btts yes opposite odds | 1.69 |
| Market reference btts yes last update utc | 2026-10-31T12:02:35Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,693.7612 |
| Elo away rating | 1,387.3773 |
| Elo rating diff | 366.3839 |
| Elo home expectancy | 0.8918 |

</details>


---

## 2026-10-31 — Moreirense FC vs CF Estrela

The model's most likely 1X2 outcome is **CF Estrela win** at **36.7%**. Expected goals are 1.42 for Moreirense FC and 1.07 for CF Estrela (2.49 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 45.4%; Under 3.5 goals: 75.2%; Double Chance 1X: 63.3%; Double Chance X2: 65.0%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 89.0%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Moreirense FC win | 35.0% | 2.86 |
| Draw | 28.4% | 3.53 |
| CF Estrela win | 36.7% | 2.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Moreirense FC expected goals | 1.42 |
| CF Estrela expected goals | 1.07 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 71.1% |
| Under 1.5 | 28.9% |
| Over 2.5 | 45.4% |
| Under 2.5 | 54.6% |
| Over 3.5 | 24.8% |
| Under 3.5 | 75.2% |
| Over 4.5 | 11.0% |
| Under 4.5 | 89.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.45% |
| 2 | 0-1 | 11.60% |
| 3 | 1-0 | 9.13% |
| 4 | 1-2 | 8.59% |
| 5 | 0-0 | 8.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Moreirense FC win | 35.0% | 30.3% | 3.19 | +11.6% |
| Draw | 28.4% | 29.7% | 3.26 | -7.5% |
| CF Estrela win | 36.7% | 40.0% | 2.44 | -10.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:30:00+00:00 |
| Fixture id | 853df01a49c2a57a62c1ac2d356b395b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:35Z |
| Market best draw last update utc | 2026-10-31T12:02:35Z |
| Market best away last update utc | 2026-10-31T12:02:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Moreirense |
| Matched away-team name | Estrela |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4765 |
| Dc lambda away | 1.0418 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.2894 |
| Shot lambda away | 1.1237 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.19 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.46 |
| Fair Over 2.5 odds | 2.20 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.04 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 9.10 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.2278917444843962, "-10": 7.595001472382143e-08, "-11": 7.4509012583042e-09, "-12": 6.712434627882381e-10, "-13": 5.588962461315371e-11, "-14": 4.306486593730603e-12, "-15": 2.8348923643279343e-13, "-2": 0.09721717903466366, "-3": 0.03150895112916927, "-4": 0.007997539692943196, "-5": 0.0016617785052000728, "-6": 0.0002917058586250828, "-7": 4.4276320187313086e-05, "-8": 5.915371736311365e-06, "-9": 7.054472035612631e-07, "0": 0.28368026127807827, "1": 0.18080099400525437, "10": 8.023701592863296e-07, "11": 1.0485021259716527e-07, "12": 1.2582130278752031e-08, "13": 1.39546485225977e-09, "14": 1.4322684006153403e-10, "15": 1.2558896639315379e-11, "2": 0.10362895336076468, "3": 0.04473893531806632, "4": 0.015125916668977073, "5": 0.0041865090807574196, "6": 0.000978898477743503, "7": 0.00019791450393438173, "8": 3.522100514666974e-05, "9": 5.594970761046166e-06} |
| Raw goal margin distribution | {"-1": 0.18143968288288764, "-10": 4.996610903004655e-08, "-11": 4.789251020679184e-09, "-12": 4.214422776584375e-10, "-13": 3.4118988511235855e-11, "-14": 2.345039566069635e-12, "-2": 0.07617524022041376, "-3": 0.024224537467904088, "-4": 0.006022976928307696, "-5": 0.0012247699904419768, "-6": 0.0002102824227197414, "-7": 3.120626724764617e-05, "-8": 4.07522853953596e-06, "-9": 4.749558459198943e-07, "0": 0.25311329175318564, "1": 0.23959129087519174, "10": 8.786411578548887e-07, "11": 1.12180459149352e-07, "12": 1.3149260047521033e-08, "13": 1.4179893293386524e-09, "14": 1.2981969691622221e-10, "2": 0.13515777533405154, "3": 0.05725274278177257, "4": 0.018961190616380772, "5": 0.005135970758791256, "6": 0.0011745853476938818, "7": 0.0002321865355859227, "8": 4.03887840414095e-05, "9": 6.270117044924172e-06} |
| Unadjusted home-win probability | 45.8% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 28.9% |
| Raw p over 1 5 | 70.4% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 49.1% |
| P home draw | 63.3% |
| P draw away | 65.0% |
| P home away | 71.6% |
| Raw p home draw | 71.1% |
| Raw p draw away | 54.2% |
| Raw p home away | 74.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0241 |
| Totals anchor target over 2 5 | 0.4542 |
| Totals anchor reference over odds | 2.12 |
| Totals anchor reference under odds | 1.78 |
| Totals anchor reference last update utc | 2026-10-31T12:02:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4401 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.6, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.04, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.07, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.6, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.19 |
| Reference draw odds | 3.26 |
| Reference away odds | 2.44 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:35Z |
| Market reference home last update utc | 2026-10-31T12:02:35Z |
| Market reference draw last update utc | 2026-10-31T12:02:35Z |
| Market reference away last update utc | 2026-10-31T12:02:35Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:35Z |
| Home probability edge | +4.6% |
| Draw probability edge | -1.3% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -1.4% |
| Under 2.5 probability edge | +1.4% |
| Raw edge prob home | 0.1541 |
| Raw ev home | 0.4596 |
| Raw edge prob draw | -0.0437 |
| Raw ev draw | -0.1749 |
| Raw edge prob away | -0.1104 |
| Raw ev away | -0.2940 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.08625081979103738, 0.11485422853545917, 0.053343975814089915, 0.017727086111001402, 0.004418253099685368, 0.0008809551814954942, 0.0001463779941781035, 2.084735584705902e-05, 2.597970529808333e-06, 2.877828695300196e-07, 2.8690503275623352e-08, 2.6002715789696185e-09, 2.1602832132831353e-10, 1.6566873893553445e-11, 1.1797385162691467e-12, 7.840932719096018e-14], [0.10652864463308467, 0.1291197619400336, 0.07815931990648692, 0.02597363569577866, 0.0064736017924431405, 0.0012907710159016069, 0.00021447228669473065, 3.054543891766451e-05, 3.8065331023429458e-06, 4.216579851789461e-07, 4.2037178323803456e-08, 3.809904587778232e-09, 3.165235889879287e-10, 2.427369870235011e-11, 1.7285468263640252e-12, 1.1488494425179196e-13], [0.07433709494866625, 0.0741103412308063, 0.049633824229910424, 0.019028218936623584, 0.00474254408038636, 0.000945615537820744, 0.00015712184750973852, 2.2377510258798535e-05, 2.7886563940934316e-06, 3.089055591730103e-07, 3.07963290927816e-08, 2.791126335681728e-09, 2.3188436999780617e-10, 1.7782849452416903e-11, 1.2663289744841591e-12, 8.416441569249311e-14], [0.0363061101485993, 0.036195364020264416, 0.018042477852863503, 0.008055710440662308, 0.0023162504249862955, 0.0004618370128406918, 7.673804184006978e-05, 1.0929137772580216e-05, 1.3619750177279212e-06, 1.508689472543236e-07, 1.5040874505348196e-08, 1.3631813329791052e-09, 1.1325193007195872e-10, 8.68511328592066e-12, 6.184729072844885e-13, 4.110575680734184e-14], [0.013298881618582895, 0.013258315453702825, 0.0066089365147919184, 0.0021962589947956733, 0.0007354488665188826, 0.00016917030592673572, 2.810904638078726e-05, 4.003329159632777e-06, 4.988897035263844e-07, 5.526310203002794e-08, 5.509453055364134e-09, 4.993315752569149e-10, 4.148403684499684e-11, 3.1813458660455376e-12, 2.2654583332151682e-13, 1.5056986038593487e-14], [0.003897090634743317, 0.00388520316737759, 0.0019366759804388123, 0.0006435894841058841, 0.00016040657868249606, 4.297155727216553e-05, 8.237046132440447e-06, 1.173131472499127e-06, 1.4619412723140816e-07, 1.619424276001904e-08, 1.6144844747407725e-09, 1.4632361287029085e-10, 1.2156439625275109e-11, 9.322583308901237e-13, 6.638675872892541e-14, 4.412283751475053e-15], [0.0009516662034060564, 0.0009487632940317664, 0.00047293461976495723, 0.00015716400214834896, 3.917114946601196e-05, 7.810332796388483e-06, 1.7436014045855769e-06, 2.8647770328362786e-07, 3.570048096449773e-08, 3.954620245951354e-09, 3.9425572934763697e-10, 3.573210124688288e-11, 2.9685921702671646e-12, 2.2765668790002535e-13, 1.621158976205119e-14, 1.0774759223409915e-15], [0.00019919663467432157, 0.00019858901639802518, 9.899162578327181e-05, 3.28965557543721e-05, 8.199052485028885e-06, 1.6348085107559974e-06, 2.716369637142311e-07, 5.197802198885997e-08, 7.472594528344652e-09, 8.27755615980756e-10, 8.25230676533865e-11, 7.479213082009824e-12, 6.213665757188292e-13, 4.7651630296928956e-14, 3.393305459165716e-15, 2.2553031399535594e-16], [3.648273599831116e-05, 3.637145110036038e-05, 1.8130252829819893e-05, 6.024983106781337e-06, 1.5016512088000944e-06, 2.994141311835714e-07, 4.975013584326695e-08, 7.085482972953998e-09, 1.1863378666965158e-09, 1.5160291065318024e-10, 1.5114046961142638e-11, 1.3698130833997176e-12, 1.1380289018028746e-13, 8.727365554414608e-15, 6.214817204656798e-16, 4.130573249172194e-17], [5.939368640432824e-06, 5.921251522432868e-06, 2.951594833938318e-06, 9.808638180319353e-07, 2.4446796147164487e-07, 4.8744450014288e-08, 8.099293778253122e-09, 1.1535125921979047e-09, 1.4374924773569005e-10, 2.1394000041924514e-11, 2.4605582365093203e-12, 2.2300478974974615e-13, 1.852704570070373e-14, 1.4208101412647141e-15, 1.0117687010390253e-16, 6.7245497224439845e-18], [8.702332485077528e-07, 8.675787376657464e-07, 4.3246616199759263e-07, 1.43715663799485e-07, 3.5819320393629274e-08, 7.1420118283088056e-09, 1.1867043724624256e-09, 1.6901207368563478e-10, 2.1062066088300438e-11, 2.3330910599548613e-12, 3.125076194738632e-13, 3.267454747556597e-14, 2.71457323857912e-15, 2.0817637355061484e-16, 1.4824383141496612e-17, 9.852775781379826e-19], [1.1591466315014815e-07, 1.155610835430633e-07, 5.760429123772069e-08, 1.9142859442894334e-08, 4.771116783706502e-09, 9.513126471694602e-10, 1.5806846937722416e-10, 2.251232945095161e-11, 2.8054573874969035e-12, 3.1076664190552423e-13, 3.098186967176254e-14, 3.772626913927389e-15, 3.6157989031776493e-16, 2.7728995941395542e-17, 1.9746009259033804e-18, 1.3123851424327712e-19], [1.4153130853018973e-08, 1.4109958934039672e-08, 7.033459352134031e-09, 2.3373349603344564e-09, 5.825513211159846e-10, 1.1615486782790201e-10, 1.9300092585649866e-11, 2.7487458089135096e-12, 3.4254514854932475e-13, 3.794447422018456e-14, 3.782873051769507e-15, 3.4284854430294397e-16, 3.826925298773144e-17, 3.385698558887643e-18, 2.410979295225364e-19, 1.6024166525290218e-20], [1.5951611363760775e-09, 1.5902953460393856e-09, 7.927221990187323e-10, 2.634347078493479e-10, 6.565778533663032e-11, 1.309150129990117e-11, 2.1752612860582497e-12, 3.098037129516234e-13, 3.860733812854551e-14, 4.276619162561575e-15, 4.263574002595987e-16, 3.8641533044153996e-17, 3.2103052560336734e-18, 3.307744063286804e-19, 2.7173496184630595e-20, 1.8060405114186488e-21], [1.6694442284076863e-10, 1.664351849080613e-10, 8.296375016313486e-11, 2.757022739285653e-11, 6.871532178202842e-12, 1.3701143281338717e-12, 2.2765583466625177e-13, 3.2423058005371525e-14, 4.040519565271605e-15, 4.475771767017833e-16, 4.4621191230832646e-17, 4.044098294918516e-18, 3.3598020030051236e-19, 2.5765795775685156e-20, 2.4651562163645054e-21, 1.8901437850398385e-22], [1.630707416946224e-11, 1.6257331982228572e-11, 8.103870762890749e-12, 2.6930503895483185e-12, 6.71208914805604e-13, 1.3383229933252862e-13, 2.2237344128316787e-14, 3.167073225313237e-15, 3.946765702792737e-16, 4.371918565974471e-17, 4.3585827100373955e-18, 3.950261393681452e-19, 3.2818431143380934e-20, 2.5167941258514957e-21, 1.7922264555549713e-22, 1.600407381711599e-23]] |
| Legacy trial inputs | {"lambda_home": 1.4651948737169762, "lambda_away": 0.996949655915172, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3946 |
| Legacy p draw | 0.2738 |
| Legacy p away | 0.3315 |
| Legacy p over 1 5 | 0.6924 |
| Legacy p under 3 5 | 0.7707 |
| Legacy p btts yes | 0.4868 |
| Legacy p over 2 5 | 0.4356 |
| Legacy goal margin distribution | {"-1": 0.21453571926000942, "-10": 3.274120830480238e-08, "-11": 2.935211547303287e-09, "-12": 2.416094547619551e-10, "-13": 1.8379585135609962e-11, "-14": 1.2946234605209386e-12, "-15": 7.840932719096018e-14, "-2": 0.08455131132452529, "-3": 0.025227195044924086, "-4": 0.005877590586665761, "-5": 0.0011192238674155536, "-6": 0.00017986861723065604, "-7": 2.4978347102186505e-05, "-8": 3.051830458145336e-06, "-9": 3.3272767492967744e-07, "0": 0.2738403336129095, "1": 0.20104621849158935, "10": 9.93098231475277e-07, "11": 1.308455857195142e-07, "12": 1.5829082999611042e-08, "13": 1.7697001920470295e-09, "14": 1.8320175482299721e-10, "15": 1.630707416946224e-11, "2": 0.11782584185083034, "3": 0.05166677232265518, "4": 0.0176914675667022, "5": 0.004951122308494711, "6": 0.001169403126698955, "7": 0.0002386682857521503, "8": 4.2856192415829836e-05, "9": 6.866956054433633e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4858 |
| Legacy raw p draw | 0.2509 |
| Legacy raw p away | 0.2633 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4652 |
| Legacy lambda away | 0.9969 |
| Legacy model home team | Moreirense |
| Legacy model away team | Estrela |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 61.3% |
| Market reference home draw last update utc | 2026-10-31T12:02:17Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.6% |
| Market reference draw away last update utc | 2026-10-31T12:02:17Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.1% |
| Market reference home away last update utc | 2026-10-31T12:02:17Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home draw odds | 1.52 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 73.0% |
| Market over 1 5 odds | 1.34 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference over 1 5 odds | 1.34 |
| Market reference over 1 5 opposite odds | 3.38 |
| Market reference over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.6% |
| Market under 3 5 odds | 1.28 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 3.83 |
| Market reference under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.0% |
| Market reference btts yes odds | 1.83 |
| Market reference btts yes opposite odds | 2.14 |
| Market reference btts yes last update utc | 2026-10-31T12:02:35Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,438.8922 |
| Elo away rating | 1,379.1640 |
| Elo rating diff | 119.7282 |
| Elo home expectancy | 0.6658 |

</details>


---

## 2026-11-01 — Académico de Viseu vs Rio Ave FC

The model's most likely 1X2 outcome is **Académico de Viseu win** at **55.5%**. Expected goals are 2.00 for Académico de Viseu and 0.93 for Rio Ave FC (2.93 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 52.1%; Under 3.5 goals: 69.5%; Double Chance 1X: 79.2%; Double Chance X2: 44.5%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Académico de Viseu win | 55.5% | 1.80 |
| Draw | 23.7% | 4.22 |
| Rio Ave FC win | 20.8% | 4.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Académico de Viseu expected goals | 2.00 |
| Rio Ave FC expected goals | 0.93 |
| Expected total goals | 2.93 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 76.0% |
| Under 1.5 | 24.0% |
| Over 2.5 | 52.1% |
| Under 2.5 | 47.9% |
| Over 3.5 | 30.5% |
| Under 3.5 | 69.5% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.23% |
| 2 | 1-0 | 10.71% |
| 3 | 2-0 | 9.88% |
| 4 | 2-1 | 8.84% |
| 5 | 0-1 | 6.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Académico de Viseu win | 55.5% | 52.4% | 1.85 | +2.7% |
| Draw | 23.7% | 25.3% | 3.70 | -12.4% |
| Rio Ave FC win | 20.8% | 22.3% | 4.16 | -13.4% |
| Over 2.5 | 52.1% | 52.1% | 1.85 | -3.7% |
| Under 2.5 | 47.9% | 47.9% | 2.00 | -4.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T18:00:00+00:00 |
| Fixture id | ce5c2cbdf5db2a13f40f528d3e5044b9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:35Z |
| Market best draw last update utc | 2026-10-31T12:02:35Z |
| Market best away last update utc | 2026-10-31T12:02:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Academico Viseu |
| Matched away-team name | Rio Ave |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1613 |
| Dc lambda away | 0.7702 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6276 |
| Shot lambda away | 1.3047 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.96 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.17 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.09 |
| Fair Over 3.5 odds | 3.28 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.72 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.14321029970472668, "-10": 7.604796659310103e-09, "-11": 6.111863067726182e-10, "-12": 4.511459422299611e-11, "-13": 3.078673561077505e-12, "-14": 1.9529152316023714e-13, "-15": 1.1519474997318664e-14, "-16": 5.819862043511535e-16, "-2": 0.048951208385050404, "-3": 0.012898000734128284, "-4": 0.002669356705068464, "-5": 0.00045302643843231143, "-6": 6.502076672504405e-05, "-7": 8.074857378605803e-06, "-8": 8.830974995399721e-07, "-9": 8.623881260095168e-08, "0": 0.23681416299695618, "1": 0.2249846493582457, "10": 1.2034726625723323e-05, "11": 2.0801165936938912e-06, "12": 3.302148181361356e-07, "13": 4.8462809114879814e-08, "14": 6.611405188442555e-09, "15": 8.387036008951653e-10, "16": 9.112844314816097e-11, "2": 0.16927332456443903, "3": 0.09592083347070723, "4": 0.04269358244579513, "5": 0.015582781229824934, "6": 0.004809932164938421, "7": 0.0012846569331168988, "8": 0.00030215264427840187, "9": 6.345793740851741e-05} |
| Raw goal margin distribution | {"-1": 0.11752540297176335, "-10": 8.458380027633216e-09, "-11": 7.056813928330702e-10, "-12": 5.408202124280364e-11, "-13": 3.832254973662854e-12, "-14": 2.5249126674041165e-13, "-15": 1.554046669109794e-14, "-16": 8.931561283500237e-16, "-17": 4.4061892702286905e-17, "-2": 0.04118451844673237, "-3": 0.011179661746445175, "-4": 0.002390648943510928, "-5": 0.00041991905650499436, "-6": 6.244254081370203e-05, "-7": 8.039869458973728e-06, "-8": 9.120431605883723e-07, "-9": 9.241677375789132e-08, "0": 0.19961296065378947, "1": 0.24704280742425805, "10": 1.79036504168828e-05, "11": 3.2123917464805615e-06, "12": 5.294661368942896e-07, "13": 8.068728656561236e-08, "14": 1.1433060852103587e-08, "15": 1.513371845694074e-09, "16": 1.8705719404789287e-10, "17": 1.9846120369536063e-11, "2": 0.19048679356254145, "3": 0.1112051710249324, "4": 0.05114198314575661, "5": 0.019319362068140954, "6": 0.0061783599091131845, "7": 0.0017108308550493516, "8": 0.00041738698948549674, "9": 9.095776060173869e-05} |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 20.0% |
| Unadjusted away-win probability | 17.3% |
| Raw p over 1 5 | 78.5% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 51.9% |
| P home draw | 79.2% |
| P draw away | 44.5% |
| P home away | 76.3% |
| Raw p home draw | 82.7% |
| Raw p draw away | 37.2% |
| Raw p home away | 80.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9623 |
| Totals anchor target over 2 5 | 0.5207 |
| Totals anchor reference over odds | 1.85 |
| Totals anchor reference under odds | 2.00 |
| Totals anchor reference last update utc | 2026-10-31T12:02:35Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5441 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.13, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.39, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.13, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.85 |
| Reference draw odds | 3.70 |
| Reference away odds | 4.16 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:35Z |
| Market reference home last update utc | 2026-10-31T12:02:35Z |
| Market reference draw last update utc | 2026-10-31T12:02:35Z |
| Market reference away last update utc | 2026-10-31T12:02:35Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:35Z |
| Market best over 2 5 last update utc | 2026-10-31T12:02:35Z |
| Market best under 2 5 last update utc | 2026-10-31T12:02:35Z |
| Home probability edge | +3.1% |
| Draw probability edge | -1.6% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.1038 |
| Raw ev home | 0.1611 |
| Raw edge prob draw | -0.0531 |
| Raw ev draw | -0.2614 |
| Raw edge prob away | -0.0507 |
| Raw ev away | -0.2813 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.061014521122020784, 0.06501448752807971, 0.022860217223717564, 0.005923337904376093, 0.001151102314100611, 0.00017895808868832004, 2.3185020939399516e-05, 2.574642076734359e-06, 2.5016945684629895e-07, 2.16072345500644e-08, 1.679602824854452e-09, 1.186919654038931e-10, 7.688603860819366e-12, 4.597392078208268e-13, 2.552647918399237e-14, 1.3228392384560242e-15, 6.426795723762638e-17, 2.93868465195637e-18], [0.10786072152844975, 0.10342355716571552, 0.04817507673576191, 0.012482701073334782, 0.0024258055717412802, 0.00037713200931881137, 4.885956034210334e-05, 5.425739326969905e-06, 5.272011487279485e-07, 4.553457092336768e-08, 3.5395549474051404e-09, 2.501286179957427e-10, 1.6202780461839084e-11, 9.688434452944794e-13, 5.379389362087083e-14, 2.7877198715145146e-15, 1.3543676078288033e-16, 6.192913970359088e-18], [0.1093995590885497, 0.08503994717936346, 0.04458464845188125, 0.01315287331245419, 0.00255604241248042, 0.00039737950236089784, 5.148273626889093e-05, 5.717036847616392e-06, 5.555055655551749e-07, 4.7979234556164464e-08, 3.729586852411336e-09, 2.635575429539904e-10, 1.707267661638747e-11, 1.0208587885502882e-12, 5.6681984421656075e-14, 2.9373871957061894e-15, 1.427081002710008e-16, 6.5253996237290314e-18], [0.07684867415989105, 0.059737052377620184, 0.023217807371288528, 0.00811507073092818, 0.001795514279327007, 0.00027914269627023165, 3.6164496981064146e-05, 4.015982381674397e-06, 3.9021972809599533e-07, 3.370343165517915e-08, 2.61988080354129e-09, 1.8513829406258172e-10, 1.1992850549497998e-11, 7.171111571031309e-13, 3.9816754179329975e-14, 2.0633932473306237e-15, 1.0024654933779394e-16, 4.58382386204255e-18], [0.04048726591772363, 0.031472109977090615, 0.012232163421740093, 0.0031694903219617395, 0.0008308484216144699, 0.00014706466567489382, 1.905304967274575e-05, 2.1157963801619723e-06, 2.0558493780768658e-07, 1.7756452075203852e-08, 1.3802685853112193e-09, 9.753900669346417e-11, 6.3183618275416675e-12, 3.778057387144141e-13, 2.097721960804551e-14, 1.0870864333156204e-15, 5.2814296990068174e-17, 2.4149602794238597e-18], [0.017064379776618285, 0.01326471483927673, 0.005155553910269264, 0.001335861667275363, 0.0002596025216428943, 5.444164794814948e-05, 8.030388522139712e-06, 8.917557691953948e-07, 8.664895926121502e-08, 7.48390474951677e-09, 5.817490215652124e-10, 4.111027542916307e-11, 2.663033014142364e-12, 1.592357611973582e-13, 8.84137849111987e-15, 4.581800061729176e-16, 2.22599180518906e-17, 1.0178459429016918e-18], [0.005993511181030102, 0.004658957298366943, 0.0018107818983225798, 0.0004691938379204946, 9.118002742896297e-05, 1.4175458806183591e-05, 2.4772978993225786e-06, 3.1321080774023236e-07, 3.043365847191852e-08, 2.6285670725316063e-09, 2.0432733629627414e-10, 1.4439135712247085e-11, 9.353353801691816e-13, 5.592827443186098e-14, 3.1053517054780063e-15, 1.6092627015278667e-16, 7.818336762266993e-18, 3.5749737870381443e-19], [0.001804368937637001, 0.001402596504292446, 0.0005451426570304774, 0.0001412525581922624, 2.745008797955293e-05, 4.2675748445395424e-06, 5.528881810054871e-07, 8.281931358124147e-08, 9.162166607645329e-09, 7.913399396305612e-10, 6.151350812358727e-11, 4.346955762419374e-12, 2.8158621136669067e-13, 1.6837416010817112e-14, 9.348777350307002e-16, 4.844745497973074e-17, 2.353739497887349e-18, 1.0762592175709403e-19], [0.00047531050984558237, 0.00036947480399210527, 0.0001436025797424026, 3.72090341675256e-05, 7.230957616658011e-06, 1.1241731847915162e-06, 1.4564292131157435e-07, 1.6173304064180086e-08, 2.119830444173405e-09, 2.0845636517083731e-10, 1.6204012549064776e-11, 1.1450838665054703e-12, 7.417600851933614e-14, 4.4353461321853456e-15, 2.462673811391672e-16, 1.2762126440335207e-17, 6.20026812393281e-19, 2.835103768188263e-20], [0.00011129533732498687, 8.651359919801475e-05, 3.3624961413879343e-05, 8.712603494833522e-06, 1.6931497420288236e-06, 2.6322841852102896e-07, 3.410271332235899e-08, 3.787026152792808e-09, 3.679728084412313e-10, 4.28711939332618e-11, 3.794216633779839e-12, 2.681247154192524e-13, 1.7368527980293604e-14, 1.0385491877615206e-15, 5.766422304638098e-17, 2.988288997907253e-18, 1.4518108017065538e-19, 6.638477872798644e-21], [2.345411403353157e-05, 1.8231669626162593e-05, 7.086044198521577e-06, 1.8360732875993839e-06, 3.5681033976679467e-07, 5.547212932048241e-08, 7.186724496641336e-09, 7.980688622759367e-10, 7.754571231693353e-11, 6.6976537244242285e-12, 7.022876816375816e-13, 5.650396325488731e-14, 3.6602021758995375e-15, 2.1886137968262964e-16, 1.2152020879684933e-17, 6.297448986331356e-19, 3.0595114689223945e-20, 1.3989769992164747e-21], [4.4933309738966465e-06, 3.49281689856063e-06, 1.3575418723596692e-06, 3.5175427908808176e-07, 6.835760025676466e-08, 1.0627331158506901e-08, 1.3768301687052868e-09, 1.5289375386510683e-10, 1.485618047854654e-11, 1.2831341609989669e-12, 9.974232271545774e-14, 9.507780629824282e-15, 7.012202543306593e-16, 4.1929386670149035e-17, 2.3280799153642264e-18, 1.2064630770687874e-19, 5.8614013851245136e-21, 2.6801552483975265e-22], [7.890948802317239e-07, 6.133899212527578e-07, 2.3840428123420118e-07, 6.177321509154218e-08, 1.2004598081223043e-08, 1.866315358566275e-09, 2.4179158922089063e-10, 2.6850387628966192e-11, 2.608963377842017e-12, 2.2533719482868487e-13, 1.7516216066526158e-14, 1.2378129404226267e-15, 1.0815986413524918e-16, 7.363415814432709e-18, 4.0884500889350054e-19, 2.11872626974104e-20, 1.0293481274480615e-21, 4.706746057708319e-23], [1.2791690282439243e-07, 9.943409964503821e-08, 3.864673062711934e-08, 1.0013800051135364e-08, 1.946015675264244e-09, 3.025406530217093e-10, 3.919583309556065e-11, 4.352605131746811e-12, 4.2292824758641606e-13, 3.652847937013297e-14, 2.8394812392838132e-15, 2.0065672909741805e-16, 1.299810056045454e-17, 1.0484045589100894e-18, 6.627617107021399e-20, 3.434579404169555e-21, 1.6686336166897666e-22, 7.629911093912606e-24], [1.9254930797959624e-08, 1.496750363203399e-08, 5.817371335312459e-09, 1.5073459625106573e-09, 2.9292764546056904e-10, 4.5540497063939906e-11, 5.900026010319257e-12, 6.551840198764355e-13, 6.366206466832861e-14, 5.498517607107697e-15, 4.274182188383058e-16, 3.020422905501244e-17, 1.9565633725517868e-18, 1.1699248800319174e-19, 8.762384405617973e-21, 5.16996481990896e-22, 2.511741928321908e-23, 1.1485066231595535e-24], [2.7051588053768103e-09, 2.1028106862371414e-09, 8.172926434788712e-10, 2.1176966284744985e-10, 4.115391573050599e-11, 6.398063847978528e-12, 8.289049429073319e-13, 9.204794549034303e-14, 8.943994481883373e-15, 7.724963271726222e-16, 6.004873091475549e-17, 4.2434448113645386e-18, 2.7488100014865156e-19, 1.6436478656070354e-20, 9.126161596289853e-22, 6.379538400973679e-23, 3.52879003592895e-24, 1.6135569830263314e-25], [3.5629919806776963e-10, 2.769633190130836e-10, 1.0764643941768403e-10, 2.7892396149777313e-11, 5.420423800252785e-12, 8.426954505185145e-13, 1.091759071021171e-13, 1.212372785538801e-14, 1.1780225453247323e-15, 1.0174627135931255e-16, 7.909078989148086e-18, 5.589084013585001e-19, 3.6204854118865183e-20, 2.1648652022113486e-21, 1.2020159599251398e-22, 6.229115521879306e-24, 4.082242153845962e-25, 2.1252321968907505e-26], [4.416802558792414e-11, 3.433328794290331e-11, 1.3344208228458774e-11, 3.457633566207349e-12, 6.719336400566955e-13, 1.0446331179855634e-13, 1.3533806095050361e-14, 1.5028973543632714e-15, 1.4603156618712844e-16, 1.2612803905382979e-17, 9.804355582724664e-19, 6.928413172519305e-20, 4.488073315351506e-21, 2.6836384186161002e-22, 1.4900586912061668e-23, 7.721817372941998e-25, 3.7515172992617157e-26, 2.3139309368400254e-27]] |
| Legacy trial inputs | {"lambda_home": 2.1073761576412355, "lambda_away": 0.7773335458375183, "rho": 0.05, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-31T12:02:35Z", "over": 1.85, "under": 2.0, "bookmaker": "pinnacle", "event_id": "ce5c2cbdf5db2a13f40f528d3e5044b9", "kickoff_utc": "2026-11-01T18:00:00Z", "home_team": "Acad\u00e9mico de Viseu", "away_team": "Rio Ave FC"}} |
| Legacy p home | 0.6048 |
| Legacy p draw | 0.2180 |
| Legacy p away | 0.1771 |
| Legacy p over 1 5 | 0.7661 |
| Legacy p under 3 5 | 0.6856 |
| Legacy p btts yes | 0.4838 |
| Legacy p over 2 5 | 0.5304 |
| Legacy goal margin distribution | {"-1": 0.128293369495102, "-10": 1.9475426739492624e-09, "-11": 1.3595653111231059e-10, "-12": 8.716246515925765e-12, "-13": 5.165731501470209e-13, "-14": 2.8461490979639925e-14, "-15": 1.4648013988626338e-15, "-16": 7.046087120798547e-17, "-17": 2.93868465195637e-18, "-2": 0.0381980794527192, "-3": 0.00878489261204201, "-4": 0.0015839463196620637, "-5": 0.00023394325853244805, "-6": 2.9201391594862596e-05, "-7": 3.1525425997377817e-06, "-8": 2.996252336681551e-07, "-9": 2.54227267013986e-08, "0": 0.21802564982073483, "1": 0.21956231381776906, "10": 2.7195648449765647e-05, "11": 5.1469169818840215e-06, "12": 8.945636457620342e-07, "13": 1.437302634296951e-07, "14": 2.1468845557180657e-08, "15": 2.9954663326183527e-09, "16": 3.9063248601067293e-10, "17": 4.416802558792414e-11, "2": 0.1828002336662529, "3": 0.11397414106220234, "4": 0.05571151674181456, "5": 0.022307438792163625, "6": 0.0075487905524393465, "7": 0.0022093750401062638, "8": 0.0005692742206532055, "9": 0.0001309483144359477} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6859 |
| Legacy raw p draw | 0.1833 |
| Legacy raw p away | 0.1308 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.1074 |
| Legacy lambda away | 0.7773 |
| Legacy model home team | Academico Viseu |
| Legacy model away team | Rio Ave |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 76.6% |
| Market reference home draw last update utc | 2026-10-31T12:02:17Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.2% |
| Market reference draw away last update utc | 2026-10-31T12:02:17Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.2% |
| Market reference home away last update utc | 2026-10-31T12:02:17Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.90 |
| Market reference dc home draw odds | 1.22 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 77.5% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 3.85 |
| Market reference over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.0% |
| Market under 3 5 odds | 1.37 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 3.11 |
| Market reference under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.8% |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 1.92 |
| Market reference btts yes last update utc | 2026-10-31T12:02:35Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,418.3104 |
| Elo away rating | 1,393.4483 |
| Elo rating diff | 84.8621 |
| Elo home expectancy | 0.6198 |

</details>


---

## 2026-11-01 — Arouca vs Nacional

The model's most likely 1X2 outcome is **Arouca win** at **52.7%**. Expected goals are 1.58 for Arouca and 1.14 for Nacional (2.71 combined). The most likely exact score is 1-0 at 11.7%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 52.1%; Under 3.5 goals: 69.8%; Double Chance 1X: 77.0%; Double Chance X2: 47.3%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 54.3%; BTTS No (at least one team does not score): 45.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arouca win | 52.7% | 1.90 |
| Draw | 24.4% | 4.10 |
| Nacional win | 23.0% | 4.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arouca expected goals | 1.58 |
| Nacional expected goals | 1.14 |
| Expected total goals | 2.71 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 75.9% |
| Under 1.5 | 24.1% |
| Over 2.5 | 52.1% |
| Under 2.5 | 47.9% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.70% |
| 2 | 1-1 | 11.51% |
| 3 | 2-1 | 10.25% |
| 4 | 2-0 | 8.87% |
| 5 | 0-1 | 6.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arouca win | 52.7% | 54.6% | 1.78 | -6.3% |
| Draw | 24.4% | 24.6% | 3.81 | -7.2% |
| Nacional win | 23.0% | 20.8% | 4.47 | +2.7% |
| Over 2.5 | 52.1% | 52.1% | 1.85 | -3.7% |
| Under 2.5 | 47.9% | 47.9% | 2.00 | -4.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T15:30:00+00:00 |
| Fixture id | fd5c6a92f2448c1cfe7a2d9b8075172b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:35Z |
| Market best draw last update utc | 2026-10-31T12:02:35Z |
| Market best away last update utc | 2026-10-31T12:02:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Arouca |
| Matched away-team name | Nacional |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5600 |
| Dc lambda away | 1.0677 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6114 |
| Shot lambda away | 1.2948 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.3% |
| P btts no | 45.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.87 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.15 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.09 |
| Fair Over 3.5 odds | 3.31 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.82 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.14024747826473538, "-10": 7.213422272448772e-08, "-11": 7.479568106746506e-09, "-12": 7.124049454187092e-10, "-13": 6.27215233084292e-11, "-14": 5.1035939085744976e-12, "-15": 3.5016159146435543e-13, "-2": 0.0616343325812544, "-3": 0.020801954678187698, "-4": 0.005529832048219977, "-5": 0.001207380400598037, "-6": 0.00022316067887965643, "-7": 3.5713213125935806e-05, "-8": 5.035321835892109e-06, "-9": 6.341422915836391e-07, "0": 0.24366324133182576, "1": 0.2565990735038373, "10": 2.53162161845368e-06, "11": 3.640952694430656e-07, "12": 4.810015955062537e-08, "13": 5.873774437270166e-09, "14": 6.629150120012524e-10, "15": 6.308575820423628e-11, "2": 0.15791796104489692, "3": 0.07392546285827196, "4": 0.027257305625898537, "5": 0.008254602799033518, "6": 0.0021161712446475275, "7": 0.00046972441739053303, "8": 9.185917084234823e-05, "9": 1.6045863033215564e-05} |
| Raw goal margin distribution | {"-1": 0.1723879220659545, "-10": 7.692662799560404e-08, "-11": 7.838187486094148e-09, "-12": 7.335662379786386e-10, "-13": 6.345835765092385e-11, "-14": 5.07522790487735e-12, "-15": 3.4334793117379857e-13, "-2": 0.07488998892706589, "-3": 0.024927104434179163, "-4": 0.006526002680434516, "-5": 0.0014021722774558967, "-6": 0.0002549070259806685, "-7": 4.0110488869892986e-05, "-8": 5.55933584919549e-06, "-9": 6.881425560141231e-07, "0": 0.23851991128461011, "1": 0.23680353522800796, "10": 2.027157333500719e-06, "11": 2.864886918424477e-07, "12": 3.718880711656069e-08, "13": 4.46213614697174e-09, "14": 4.949833771039115e-10, "15": 4.644624152477957e-11, "2": 0.14407410107133292, "3": 0.06651430559954652, "4": 0.024153026184077803, "5": 0.007197915713051691, "6": 0.0018149650338902625, "7": 0.0003961188301961005, "8": 7.615028271140442e-05, "9": 1.3073988572666461e-05} |
| Unadjusted home-win probability | 48.1% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 28.0% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 53.2% |
| P home draw | 77.0% |
| P draw away | 47.3% |
| P home away | 75.6% |
| Raw p home draw | 72.0% |
| Raw p draw away | 51.9% |
| Raw p home away | 76.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0181 |
| Totals anchor target over 2 5 | 0.5207 |
| Totals anchor reference over odds | 1.85 |
| Totals anchor reference under odds | 2.00 |
| Totals anchor reference last update utc | 2026-10-31T12:02:35Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5096 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.98, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.92, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.39, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.98, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.78 |
| Reference draw odds | 3.81 |
| Reference away odds | 4.47 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:35Z |
| Market reference home last update utc | 2026-10-31T12:02:35Z |
| Market reference draw last update utc | 2026-10-31T12:02:35Z |
| Market reference away last update utc | 2026-10-31T12:02:35Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:35Z |
| Market best over 2 5 last update utc | 2026-10-31T12:02:35Z |
| Market best under 2 5 last update utc | 2026-10-31T12:02:35Z |
| Home probability edge | -2.0% |
| Draw probability edge | -0.2% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0652 |
| Raw ev home | -0.1437 |
| Raw edge prob draw | -0.0073 |
| Raw ev draw | -0.0912 |
| Raw edge prob away | 0.0725 |
| Raw ev away | 0.2535 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06956203311362226, 0.07616171572413075, 0.037486681031424045, 0.013238746587623954, 0.0035065336485325073, 0.000743017665420696, 0.0001312015669563649, 1.985784492415693e-05, 2.6298638225687948e-06, 3.09586407305242e-07, 3.2799937581974804e-08, 3.159158858972616e-09, 2.7892108885904393e-10, 2.273155432040378e-11, 1.7202526275076925e-12, 1.2150442757617202e-13], [0.12856717242217472, 0.11618712505283432, 0.057181496747637714, 0.02019414160214497, 0.005348802211936628, 0.0011333855398688228, 0.00020013246752656981, 3.0290792988419388e-05, 4.011546113962147e-06, 4.7223743621362294e-07, 5.003242411869408e-08, 4.818923069454548e-09, 4.254611210331285e-10, 3.467429667489934e-11, 2.624041854825407e-12, 1.853406287007994e-13], [0.09312387930586413, 0.09866251736343544, 0.04941332405704221, 0.015401886891192228, 0.004079482470443624, 0.0008644227733511724, 0.00015263920045861332, 2.3102510452962244e-05, 3.059569489177198e-06, 3.60171168532178e-07, 3.815927175069593e-08, 3.675348500339934e-09, 3.244953012539071e-10, 2.6445768576848885e-11, 2.0013326954923587e-12, 1.4135760042848069e-13], [0.04734982003512045, 0.0501659990562317, 0.02657483660384771, 0.008873015122394261, 0.002074255950801767, 0.00043952488940030986, 7.761101369372287e-05, 1.1746715455381241e-05, 1.5556704228532189e-06, 1.8313283487497236e-07, 1.9402484771195844e-08, 1.868769765119601e-09, 1.6499306333823618e-10, 1.3446630360956037e-11, 1.0175987476930459e-12, 7.187476499879385e-14], [0.018056637089782775, 0.019130574066234817, 0.0101341922719038, 0.0035789779107284936, 0.0008962329363864563, 0.0001676108043059454, 2.9596604747352136e-05, 4.47955615918788e-06, 5.932477934643544e-07, 6.983686814665374e-08, 7.399048737538228e-09, 7.126467941820001e-10, 6.291934932002525e-11, 5.127810925746854e-12, 3.880566235834062e-13, 2.740911256967865e-14], [0.005508652708716296, 0.005836285468067186, 0.003091702260597752, 0.0010918614725621363, 0.0002892002628598193, 5.793627281344871e-05, 9.029223775149169e-06, 1.366606586124501e-06, 1.8098586398773858e-07, 2.1305575948137694e-08, 2.2572746889301407e-09, 2.174116738132819e-10, 1.9195204640765897e-11, 1.5643737759942013e-12, 1.1838689341813353e-13, 8.361871673541319e-15], [0.0014004663268858807, 0.0014837604954090857, 0.0007860043349389337, 0.00027758424914458614, 7.352346413504522e-05, 1.5579269486869473e-05, 2.6008644157163617e-06, 3.474327766096972e-07, 4.601208708549022e-08, 5.416522563323795e-09, 5.738675787958937e-10, 5.5272630958496504e-11, 4.88000227252313e-12, 3.977111848922017e-13, 3.0097533197978643e-14, 2.1258409864913148e-15], [0.00030517795544835033, 0.0003233287267755023, 0.00017127951690462206, 6.048884717348383e-05, 1.6021620821192077e-05, 3.3949046243431175e-06, 5.994700087366453e-07, 8.578103734909998e-08, 1.0026570716545032e-08, 1.1803234749604312e-09, 1.2505244219934528e-10, 1.2044551292906364e-11, 1.0634094426415068e-12, 8.666590830086643e-14, 6.558603708681985e-15, 4.632455585764248e-16], [5.818910806044778e-05, 6.164996483361951e-05, 3.265832980321914e-05, 1.1533572467443402e-05, 3.0548858743686342e-06, 6.473156678390854e-07, 1.1430257164586685e-07, 1.7300119158872945e-08, 2.1661123622912045e-09, 2.25055476663942e-10, 2.384408815397592e-11, 2.2965672461265024e-12, 2.0276316118396637e-13, 1.652482367498355e-14, 1.250546748599408e-15, 8.832828644822674e-17], [9.862288867988503e-06, 1.0448858594960383e-05, 5.5351575784732306e-06, 1.954788914029118e-06, 5.177629964780261e-07, 1.0971149615100023e-07, 1.9372783283676543e-08, 2.9321427717741563e-09, 3.8831687061443924e-10, 4.321809533087743e-11, 4.041259490075153e-12, 3.8923795777264437e-13, 3.436569031622654e-14, 2.800740379212628e-15, 2.119512343237703e-16, 1.4970483398059887e-17], [1.5043754830053175e-06, 1.5938497549660408e-06, 8.443228004255936e-07, 2.981799211196481e-07, 7.897861929771038e-08, 1.673519070700875e-08, 2.955088884501757e-09, 4.472636887412493e-10, 5.923314431458726e-11, 6.9728995792010416e-12, 6.984499397173627e-13, 5.937364526290288e-14, 5.242079466572032e-15, 4.2721980841855467e-16, 3.23306531351305e-17, 2.283570121929802e-18], [2.0861334654393457e-07, 2.2102083889818386e-07, 1.1708313978120518e-07, 4.134892646130443e-08, 1.0952049048419978e-08, 2.320686675553665e-09, 4.09785315232045e-10, 6.202253091063362e-11, 8.213923054037303e-12, 9.669393929672147e-13, 1.0244491032710864e-13, 9.328666664106417e-15, 7.269247290484922e-16, 5.924302473077346e-17, 4.4833260197759304e-18, 3.166650949747183e-19], [2.6517914871587386e-08, 2.809509500637116e-08, 1.488303977215708e-08, 5.25607459972114e-09, 1.392171254365483e-09, 2.949944129916864e-10, 5.208991795096593e-11, 7.884002735473112e-12, 1.0441139836796471e-12, 1.2291263686376304e-13, 1.3022299177342145e-14, 1.2542557956848204e-15, 1.0469519350544899e-16, 7.530685416693316e-18, 5.698986172438044e-19, 4.0252928062655e-20], [3.1115339784337867e-09, 3.296595647243522e-09, 1.7463320241315823e-09, 6.167323030265122e-10, 1.633532720326469e-10, 3.4613775024039664e-11, 6.112077454925335e-12, 9.2508564554499e-13, 1.22513257671628e-13, 1.4422206566107674e-14, 1.5279982066404795e-15, 1.4717067857029464e-16, 1.2993650445391154e-17, 1.0011743174921123e-18, 6.687022416368361e-20, 4.72315994696096e-21], [3.390197820600179e-10, 3.5918333067057184e-10, 1.9027306348861644e-10, 6.719658291074337e-11, 1.7798292118016558e-11, 3.771372752558271e-12, 6.659465013285025e-13, 1.007934787513963e-13, 1.3348534260970793e-14, 1.5713835557494073e-15, 1.664843201436301e-16, 1.603510413845477e-17, 1.4157340310896766e-18, 1.1537971245775062e-19, 8.255118087162507e-21, 5.146158348106192e-22], [3.447563780319607e-11, 3.652611165608036e-11, 1.9349269770271896e-11, 6.8333624662442234e-12, 1.8099459236499339e-12, 3.835188620793331e-13, 6.772150650501739e-14, 1.0249901776357409e-14, 1.3574406472343017e-15, 1.597973132680624e-16, 1.6930142206766625e-17, 1.6306436133453394e-18, 1.439689843021187e-19, 1.1733206694782542e-20, 8.879322267757706e-22, 5.929395686069355e-23]] |
| Legacy trial inputs | {"lambda_home": 1.5253816868904468, "lambda_away": 1.0594760237530456, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-31T12:02:35Z", "over": 1.85, "under": 2.0, "bookmaker": "pinnacle", "event_id": "fd5c6a92f2448c1cfe7a2d9b8075172b", "kickoff_utc": "2026-11-01T15:30:00Z", "home_team": "Arouca", "away_team": "Nacional"}} |
| Legacy p home | 0.5163 |
| Legacy p draw | 0.2450 |
| Legacy p away | 0.2387 |
| Legacy p over 1 5 | 0.7257 |
| Legacy p under 3 5 | 0.7375 |
| Legacy p btts yes | 0.5048 |
| Legacy p over 2 5 | 0.4789 |
| Legacy goal margin distribution | {"-1": 0.1509963530303477, "-10": 3.795719900153947e-08, "-11": 3.612110756442856e-09, "-12": 3.156685929944344e-10, "-13": 2.549695377565767e-11, "-14": 1.9055932562084918e-12, "-15": 1.2150442757617202e-13, "-2": 0.06223084042139561, "-3": 0.019534248672535018, "-4": 0.004804920243802463, "-5": 0.0009678804643186964, "-6": 0.00016474268369718147, "-7": 2.424969693777939e-05, "-8": 3.1421938145821077e-06, "-9": 3.634644213112744e-07, "0": 0.24499235541058437, "1": 0.2576889009980544, "10": 1.7409142757896648e-06, "11": 2.3852378010327173e-07, "12": 3.001161694478577e-08, "13": 3.4900665788746305e-09, "14": 3.7554589371609826e-10, "15": 3.447563780319607e-11, "2": 0.15459296777024883, "3": 0.069866369375972, "4": 0.024742583355503018, "5": 0.007175761209478053, "6": 0.0017584895247131165, "7": 0.0003726725110392525, "8": 6.952506584352084e-05, "9": 1.157864502970176e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4864 |
| Legacy raw p draw | 0.2441 |
| Legacy raw p away | 0.2695 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5254 |
| Legacy lambda away | 1.0595 |
| Legacy model home team | Arouca |
| Legacy model away team | Nacional |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 78.4% |
| Market reference home draw last update utc | 2026-10-31T12:02:17Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.4% |
| Market reference draw away last update utc | 2026-10-31T12:02:17Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.2% |
| Market reference home away last update utc | 2026-10-31T12:02:17Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.01 |
| Market reference dc home draw odds | 1.19 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 77.5% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 3.86 |
| Market reference over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.4% |
| Market under 3 5 odds | 1.38 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 3 5 odds | 1.38 |
| Market reference under 3 5 opposite odds | 3.06 |
| Market reference under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.2% |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.05 |
| Market reference btts yes last update utc | 2026-10-31T12:02:12Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,468.8191 |
| Elo away rating | 1,372.3854 |
| Elo rating diff | 156.4337 |
| Elo home expectancy | 0.7111 |

</details>


---

## 2026-11-01 — Braga vs Famalicão

The model's most likely 1X2 outcome is **Braga win** at **52.4%**. Expected goals are 1.54 for Braga and 0.97 for Famalicão (2.51 combined). The most likely exact score is 1-0 at 15.1%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 41.4%; Under 3.5 goals: 78.8%; Double Chance 1X: 79.4%; Double Chance X2: 47.6%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 45.1%; BTTS No (at least one team does not score): 54.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Braga win | 52.4% | 1.91 |
| Draw | 26.9% | 3.72 |
| Famalicão win | 20.6% | 4.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Braga expected goals | 1.54 |
| Famalicão expected goals | 0.97 |
| Expected total goals | 2.51 |
| Over 0.5 | 90.6% |
| Under 0.5 | 9.4% |
| Over 1.5 | 67.6% |
| Under 1.5 | 32.4% |
| Over 2.5 | 41.4% |
| Under 2.5 | 58.6% |
| Over 3.5 | 21.2% |
| Under 3.5 | 78.8% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.09% |
| 2 | 1-1 | 12.50% |
| 3 | 2-0 | 10.38% |
| 4 | 0-0 | 9.44% |
| 5 | 2-1 | 9.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Braga win | 52.4% | 53.0% | 1.83 | -4.0% |
| Draw | 26.9% | 28.0% | 3.36 | -9.6% |
| Famalicão win | 20.6% | 19.0% | 4.85 | +0.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T20:30:00+00:00 |
| Fixture id | 12fa9f636dbb126cfd4118fa8cdc8fad |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:35Z |
| Market best draw last update utc | 2026-10-31T12:02:35Z |
| Market best away last update utc | 2026-10-31T12:02:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sp Braga |
| Matched away-team name | Famalicao |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5361 |
| Dc lambda away | 0.9608 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.5565 |
| Shot lambda away | 0.9963 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 45.1% |
| P btts no | 54.9% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.60 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.08 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.73 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.26 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.13862177502242537, "-10": 9.41928776143154e-09, "-11": 7.685117877170985e-10, "-12": 5.755559564225369e-11, "-13": 3.969428773960094e-12, "-14": 2.350639787595731e-13, "-2": 0.05046437317909872, "-3": 0.013830544011033395, "-4": 0.002949087684365516, "-5": 0.0005129016293611244, "-6": 7.518965651027805e-05, "-7": 9.516949358950184e-06, "-8": 1.0592116719566147e-06, "-9": 1.0515402673528801e-07, "0": 0.26904675446970083, "1": 0.26781833161682717, "10": 1.1823984363116378e-06, "11": 1.531524727018935e-07, "12": 1.820911046466391e-08, "13": 1.993686597076858e-09, "14": 1.8743153269189796e-10, "2": 0.1570034086194561, "3": 0.06831108116422271, "4": 0.023124229953726434, "5": 0.006384712862475457, "6": 0.001485912002548603, "7": 0.00029857981613696827, "8": 5.2756155986473895e-05, "9": 8.31465037008777e-06} |
| Raw goal margin distribution | {"-1": 0.16034099419739706, "-10": 1.912480025688308e-08, "-11": 1.6702082140468e-09, "-12": 1.3393434176063038e-10, "-13": 9.925911105256086e-12, "-14": 6.810276714723599e-13, "-15": 4.010051729731747e-14, "-2": 0.06123995588562719, "-3": 0.017761010023130783, "-4": 0.00402580822220357, "-5": 0.0007461651069218108, "-6": 0.00011675241829653322, "-7": 1.5788853629704183e-05, "-8": 1.8788036561579255e-06, "-9": 1.9951946691916553e-07, "0": 0.2438997102383985, "1": 0.25098575950897223, "10": 1.9447952617098166e-06, "11": 2.69634396367706e-07, "12": 3.432608893032875e-08, "13": 4.03859641162592e-09, "14": 4.398985496626492e-10, "15": 4.1121168270202455e-11, "2": 0.1543441826112058, "3": 0.07106418067775809, "4": 0.025571951637516823, "5": 0.007524426876949488, "6": 0.001869097999773647, "7": 0.00040127720000659013, "8": 7.580589514643268e-05, "9": 1.2780108989742383e-05} |
| Unadjusted home-win probability | 51.2% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 24.4% |
| Raw p over 1 5 | 70.9% |
| Raw p under 3 5 | 75.5% |
| Raw p btts yes | 48.2% |
| P home draw | 79.4% |
| P draw away | 47.6% |
| P home away | 73.1% |
| Raw p home draw | 75.6% |
| Raw p draw away | 48.8% |
| Raw p home away | 75.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9329 |
| Totals anchor target over 2 5 | 0.4136 |
| Totals anchor reference over odds | 2.29 |
| Totals anchor reference under odds | 1.65 |
| Totals anchor reference last update utc | 2026-10-31T12:02:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4535 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.81, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.18, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.55, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.81, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.83 |
| Reference draw odds | 3.36 |
| Reference away odds | 4.85 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:35Z |
| Market reference home last update utc | 2026-10-31T12:02:35Z |
| Market reference draw last update utc | 2026-10-31T12:02:35Z |
| Market reference away last update utc | 2026-10-31T12:02:35Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.30 |
| Reference Under 2.5 odds | 1.68 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:35Z |
| Home probability edge | -0.5% |
| Draw probability edge | -1.1% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | -0.0181 |
| Raw ev home | -0.0633 |
| Raw edge prob draw | -0.0359 |
| Raw ev draw | -0.1805 |
| Raw edge prob away | 0.0540 |
| Raw ev away | 0.1846 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.07787764987232862, 0.07244367654820076, 0.03144618193714083, 0.009838681219929436, 0.0023086979607148147, 0.0004333984325469978, 6.779947129305933e-05, 9.091142987436817e-06, 1.066642104083373e-06, 1.1124139711469291e-07, 1.0441350051896529e-08, 8.909517641484336e-10, 6.968882905492749e-11, 5.031645507617946e-12, 3.3734340327025067e-13, 2.110917130134669e-14], [0.1298743209283381, 0.12202567696626078, 0.051047851642414, 0.015971526854227314, 0.0037478022362554975, 0.0007035531032332855, 0.00011006160808077054, 1.4758017981652715e-05, 1.7315230190311319e-06, 1.8058263313991443e-07, 1.6949863403486635e-08, 1.4463178254107483e-09, 1.1312867850986374e-10, 8.168072483442922e-12, 5.476231116740955e-13, 3.426736660874975e-14], [0.10068963405603573, 0.09450939515731482, 0.04892911910831581, 0.012963610892209283, 0.0030419790377717503, 0.0005710530217659586, 8.933371707992367e-05, 1.197864201716795e-05, 1.4054254721227173e-06, 1.4657352495367815e-07, 1.3757697422694484e-08, 1.173932942430525e-09, 9.182316645972681e-11, 6.629780257151143e-12, 4.4448930901336143e-13, 2.7813797082208162e-14], [0.054484510620886856, 0.05114030051352285, 0.024000677502743577, 0.008283705595317038, 0.0016460556317023872, 0.0003090044444116423, 4.833967173160698e-05, 6.481803755935553e-06, 7.60494561139434e-07, 7.931289900840383e-08, 7.444474482135755e-09, 6.352308504216957e-10, 4.968674615933368e-11, 3.58746296201525e-12, 2.40519122994642e-13, 1.505041841436628e-14], [0.022111724251168724, 0.020754526565269778, 0.009740316224450958, 0.0030474881340202833, 0.0007888681841760607, 0.00012540483505043203, 1.9617933235350606e-05, 2.6305431703096348e-06, 3.086353504656848e-07, 3.218795456634447e-08, 3.0212286954219965e-09, 2.5779894579754804e-10, 2.0164623257014763e-11, 1.4559182210393687e-12, 9.761109100889436e-14, 6.107987353668229e-15], [0.007178970225307159, 0.006738331509562985, 0.0031623694003290463, 0.0009894220065154859, 0.00023217304409676215, 4.807997134863265e-05, 6.369315978205624e-06, 8.540533013855677e-07, 1.0020403503147342e-07, 1.0450400195865003e-08, 9.808964059929296e-10, 8.369907904845323e-11, 6.5468087573041184e-12, 4.726901186266083e-13, 3.1691201828168677e-14, 1.983068296730375e-15], [0.00194231850753425, 0.0018231007498523792, 0.0008556002352908895, 0.0002676947549165349, 6.281597309179706e-05, 1.1792077066880623e-05, 2.0349861950389195e-06, 2.3106984450975902e-07, 2.71108732398892e-08, 2.8274258110186938e-09, 2.653880965570352e-10, 2.2645346783344153e-11, 1.7712829856534235e-12, 1.2788947953851404e-13, 8.574267047363554e-15, 5.365324180988685e-16], [0.0004504348195962278, 0.0004227875367403014, 0.00019841860958169655, 6.207995144460599e-05, 1.4567385007974118e-05, 2.734650411702122e-06, 4.2780000609403503e-07, 6.327980837361277e-08, 6.287167243444677e-09, 6.556962877961279e-10, 6.154502412037924e-11, 5.251586005839351e-12, 4.1077069955407334e-13, 2.965830496941307e-14, 1.9884217833830116e-15, 1.2442494988151687e-16], [9.140111942400895e-05, 8.579100117353911e-05, 4.026261345998822e-05, 1.2597110189908213e-05, 2.9559777328113795e-06, 5.549084972759379e-07, 8.680811905625626e-08, 1.1639987860667193e-08, 1.5065548549589224e-09, 1.3305226882871983e-10, 1.248856406044015e-11, 1.0656388422978756e-12, 8.335257429583488e-14, 6.0181898833952945e-15, 4.034856298436426e-16, 2.524800305989065e-17], [1.6486123617077686e-05, 1.547422022282479e-05, 7.262213272998752e-06, 2.2721550580290124e-06, 5.331730576119893e-07, 1.0008947527019986e-07, 1.5657678929384243e-08, 2.099517817522876e-09, 2.463314135018927e-10, 2.8339990375892855e-11, 2.2525764694970243e-12, 1.9221048709243222e-13, 1.503439840017786e-14, 1.0855077376945043e-15, 7.277716086231478e-17, 4.554010959086524e-18], [2.676258740235474e-06, 2.5119923932126977e-06, 1.17890428318662e-06, 3.6884806728740733e-07, 8.655212642067345e-08, 1.6247926997221935e-08, 2.5417739827668025e-09, 3.4082316983267255e-10, 3.998796889379727e-11, 4.170393715469901e-12, 4.3181673206805103e-13, 3.120230128040386e-14, 2.4405943481449164e-15, 1.7621483606909336e-16, 1.1814209171981071e-17, 7.392709114323518e-19], [3.9495258453530833e-07, 3.7071075121275333e-07, 1.7397842987458427e-07, 5.443326360260563e-08, 1.2773049747747484e-08, 2.3978102955505687e-09, 3.751058104755691e-10, 5.029745060564908e-11, 5.901279808070107e-12, 6.15451619715111e-13, 5.776757545418675e-14, 5.437682725600825e-15, 3.601740859769371e-16, 2.600514811689342e-17, 1.7434982561903264e-18, 1.0909892707768997e-19], [5.3428534348642836e-08, 5.014913911219411e-08, 2.3535515098385627e-08, 7.363642138264188e-09, 1.7279171067772575e-09, 3.243718227292673e-10, 5.0743695481698456e-11, 6.804156176101298e-12, 7.983154010687047e-13, 8.325728021900562e-14, 7.814702347177346e-15, 6.668220879394725e-16, 5.753752014202285e-17, 3.5179335540739385e-18, 2.3585756902253163e-19, 1.4758722948043736e-20], [6.6717452507199854e-09, 6.2622395463104415e-09, 2.938934466295938e-09, 9.195151067289867e-10, 2.1576902476030247e-10, 4.05050633363733e-11, 6.336483181904886e-12, 8.496507944020368e-13, 9.968749939688441e-14, 1.0396530068826857e-14, 9.758400432688488e-16, 8.326762379919876e-17, 6.513061014362182e-18, 5.187572786176485e-19, 2.9452082771055986e-20, 1.8429560334327995e-21], [7.736080248277818e-10, 7.261246621934262e-10, 3.4077789275963985e-10, 1.0662041771441338e-10, 2.501903816633601e-11, 4.696678435045824e-12, 7.347334249878469e-13, 9.851945003142661e-14, 1.1559051883781397e-14, 1.2055075230487614e-15, 1.1315145588623963e-16, 9.655120146029167e-18, 7.552081318392393e-19, 5.452724138743105e-20, 4.032811286800091e-21, 2.136960455308951e-22], [8.372193431883076e-11, 7.858315752215038e-11, 3.687989710458795e-11, 1.153874743080593e-11, 2.7076273808672114e-12, 5.082871309964909e-13, 7.951482090995113e-14, 1.066203899125093e-14, 1.2509515821236986e-15, 1.3046325584331021e-16, 1.2245553890029432e-17, 1.0449029854443727e-18, 8.173064857356822e-20, 5.901084238418812e-21, 3.956343579766732e-22, 2.731021692613797e-23]] |
| Legacy trial inputs | {"lambda_home": 1.6233402116815272, "lambda_away": 0.9386209021746817, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5351 |
| Legacy p draw | 0.2580 |
| Legacy p away | 0.2070 |
| Legacy p over 1 5 | 0.7198 |
| Legacy p under 3 5 | 0.7442 |
| Legacy p btts yes | 0.4887 |
| Legacy p over 2 5 | 0.4656 |
| Legacy goal margin distribution | {"-1": 0.13823320635790323, "-10": 1.1983178100888327e-08, "-11": 1.0109568500257967e-09, "-12": 7.831644126579814e-11, "-13": 5.607082416374249e-12, "-14": 3.716107698790004e-13, "-15": 2.110917130134669e-14, "-2": 0.05078919203934104, "-3": 0.014208609786939526, "-4": 0.0031083859412587536, "-5": 0.0005562323691192572, "-6": 8.404533437496696e-05, "-7": 1.0976948481561466e-05, "-8": 1.2616383115084712e-06, "-9": 1.2941636835272475e-07, "0": 0.25795519949908247, "1": 0.2516762865341346, "10": 3.0714500489786392e-06, "11": 4.4814998615889364e-07, "12": 6.004309053514373e-08, "13": 7.434749810018e-09, "14": 8.521911823499321e-10, "15": 8.372193431883076e-11, "2": 0.1626253123722767, "3": 0.07868423963939507, "4": 0.02977079460755555, "5": 0.009213636497926624, "6": 0.002407729814334321, "7": 0.0005438699859678771, "8": 0.00010811044636118855, "9": 1.9179678627521247e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5402 |
| Legacy raw p draw | 0.2361 |
| Legacy raw p away | 0.2237 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.6233 |
| Legacy lambda away | 0.9386 |
| Legacy model home team | Sp Braga |
| Legacy model away team | Famalicao |
| Legacy home name match score | 90/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 79.7% |
| Market reference home draw last update utc | 2026-10-31T12:02:17Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 48.1% |
| Market reference draw away last update utc | 2026-10-31T12:02:17Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.3% |
| Market reference home away last update utc | 2026-10-31T12:02:17Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.94 |
| Market reference dc home draw odds | 1.17 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 68.8% |
| Market over 1 5 odds | 1.41 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference over 1 5 odds | 1.41 |
| Market reference over 1 5 opposite odds | 2.92 |
| Market reference over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 79.6% |
| Market under 3 5 odds | 1.23 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 3 5 odds | 1.23 |
| Market reference under 3 5 opposite odds | 4.23 |
| Market reference under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 45.3% |
| Market reference btts yes odds | 2.05 |
| Market reference btts yes opposite odds | 1.73 |
| Market reference btts yes last update utc | 2026-10-31T12:02:12Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,518.8201 |
| Elo away rating | 1,511.6518 |
| Elo rating diff | 67.1683 |
| Elo home expectancy | 0.5955 |

</details>


---

## 2026-11-01 — CS Maritimo vs Santa Clara

The model's most likely 1X2 outcome is **Santa Clara win** at **43.2%**. Expected goals are 1.03 for CS Maritimo and 1.32 for Santa Clara (2.35 combined). The most likely exact score is 0-1 at 14.4%. Goal-market probabilities: at least one goal: 88.7%; Over 2.5 goals: 37.1%; Under 3.5 goals: 81.9%; Double Chance 1X: 56.8%; Double Chance X2: 73.0%; Double Chance 12 (either team wins): 70.1%; Under 4.5 goals: 92.9%; BTTS Yes (both teams score): 43.9%; BTTS No (at least one team does not score): 56.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CS Maritimo win | 27.0% | 3.71 |
| Draw | 29.9% | 3.35 |
| Santa Clara win | 43.2% | 2.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CS Maritimo expected goals | 1.03 |
| Santa Clara expected goals | 1.32 |
| Expected total goals | 2.35 |
| Over 0.5 | 88.7% |
| Under 0.5 | 11.3% |
| Over 1.5 | 63.9% |
| Under 1.5 | 36.1% |
| Over 2.5 | 37.1% |
| Under 2.5 | 62.9% |
| Over 3.5 | 18.1% |
| Under 3.5 | 81.9% |
| Over 4.5 | 7.1% |
| Under 4.5 | 92.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.37% |
| 2 | 1-1 | 13.64% |
| 3 | 0-0 | 11.33% |
| 4 | 1-0 | 10.38% |
| 5 | 0-2 | 8.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CS Maritimo win | 27.0% | 25.8% | 3.66 | -1.3% |
| Draw | 29.9% | 31.4% | 3.03 | -9.5% |
| Santa Clara win | 43.2% | 42.8% | 2.25 | -2.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T18:00:00+00:00 |
| Fixture id | 6bf5102547eb3f3eb74023133e27d2d3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:35Z |
| Market best draw last update utc | 2026-10-31T12:02:35Z |
| Market best away last update utc | 2026-10-31T12:02:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Maritimo |
| Matched away-team name | Santa Clara |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9841 |
| Dc lambda away | 1.3334 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.1414 |
| Shot lambda away | 1.2988 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 43.9% |
| P btts no | 56.1% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.83 |
| Fair Over 1.5 odds | 1.56 |
| Fair Under 1.5 odds | 2.77 |
| Fair Over 2.5 odds | 2.70 |
| Fair Under 2.5 odds | 1.59 |
| Fair Over 3.5 odds | 5.53 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 14.08 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.24343375518265276, "-10": 2.850352033709736e-07, "-11": 3.17635491894425e-08, "-12": 3.2487911112430172e-09, "-13": 3.0613548255442877e-10, "-14": 2.4922329993730498e-11, "-2": 0.12393815236831777, "-3": 0.0467066491466392, "-4": 0.013657786351340587, "-5": 0.003252617314736319, "-6": 0.0006523346255756604, "-7": 0.00011289334168843366, "-8": 1.717263417584202e-05, "-9": 2.3293734054339753e-06, "0": 0.2986487409197479, "1": 0.17486105441538635, "10": 2.1585334565420213e-08, "11": 1.874982439297461e-09, "12": 1.4948508639226253e-10, "13": 1.0979881306216881e-11, "14": 6.967556767341629e-13, "2": 0.06886556590982841, "3": 0.020229433064469223, "4": 0.004610979729486806, "5": 0.0008559605819401572, "6": 0.0001338132517782598, "7": 1.805115184017557e-05, "8": 2.140333291641022e-06, "9": 2.2630361877189462e-07} |
| Raw goal margin distribution | {"-1": 0.2396845642839167, "-10": 4.864576533695024e-07, "-11": 5.791490077702465e-08, "-12": 6.329394759539501e-09, "-13": 6.368309667920751e-10, "-14": 5.4837277905797144e-11, "-2": 0.127973776762479, "-3": 0.050994898825946516, "-4": 0.015832371416349543, "-5": 0.004012443781919422, "-6": 0.0008575517633727112, "-7": 0.00015829406303639022, "-8": 2.5698533950480842e-05, "-9": 3.722008889182547e-06, "0": 0.26306511853417647, "1": 0.18825911578406868, "10": 4.0283204942356026e-08, "11": 3.738326157192312e-09, "12": 3.184615126187435e-10, "13": 2.4976227489121784e-11, "14": 1.6764339759372427e-12, "2": 0.07775651402817832, "3": 0.024151851353560683, "4": 0.0058449063854816245, "5": 0.0011546449176005496, "6": 0.0001923568823279324, "7": 2.7677057073205204e-05, "8": 3.5024466496814044e-06, "9": 3.9541076053458083e-07} |
| Unadjusted home-win probability | 29.7% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 67.5% |
| Raw p under 3 5 | 78.8% |
| Raw p btts yes | 46.6% |
| P home draw | 56.8% |
| P draw away | 73.0% |
| P home away | 70.1% |
| Raw p home draw | 56.0% |
| Raw p draw away | 70.3% |
| Raw p home away | 73.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9348 |
| Totals anchor target over 2 5 | 0.3709 |
| Totals anchor reference over odds | 2.52 |
| Totals anchor reference under odds | 1.54 |
| Totals anchor reference last update utc | 2026-10-31T12:02:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4080 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.85, "price": 1.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.38, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.82, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.11, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.66 |
| Reference draw odds | 3.03 |
| Reference away odds | 2.25 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:35Z |
| Market reference home last update utc | 2026-10-31T12:02:35Z |
| Market reference draw last update utc | 2026-10-31T12:02:35Z |
| Market reference away last update utc | 2026-10-31T12:02:35Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.50 |
| Reference Under 2.5 odds | 1.54 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:35Z |
| Home probability edge | +1.2% |
| Draw probability edge | -1.5% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | 0.0397 |
| Raw ev home | 0.0885 |
| Raw edge prob draw | -0.0508 |
| Raw ev draw | -0.2029 |
| Raw edge prob away | 0.0111 |
| Raw ev away | -0.0110 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.10465903040389099, 0.13684439475932803, 0.08095226867873578, 0.033560850849756116, 0.010435137224777699, 0.0025956931637383103, 0.0005380557737403822, 9.559924208290757e-05, 1.4862424289924296e-05, 2.053867103833921e-06, 2.5544507397516695e-07, 2.8882184643244324e-08, 2.99346363865913e-09, 2.8638866697695285e-10, 2.544210176744726e-11], [0.10307224749069585, 0.13529208132904888, 0.0829258239351542, 0.03437903908197558, 0.010689538000167175, 0.0026589742054059008, 0.0005511731677040493, 9.79298795042143e-05, 1.5224758984914822e-05, 2.1039388348047054e-06, 2.616726322227384e-07, 2.9586310521985686e-08, 3.0664420245079374e-09, 2.9337060668433866e-10, 2.6062361020177347e-11], [0.049701763390436804, 0.06181544366851587, 0.04536017751481712, 0.01760858706311067, 0.005475070437296154, 0.0013618989955714836, 0.00028230517691972486, 5.015866805404621e-05, 7.797963563248713e-06, 1.0776156384063006e-06, 1.3402600682178947e-07, 1.515380122930052e-08, 1.5705997841818246e-09, 1.5026138040801576e-10, 1.334887086284562e-11], [0.016971151632322684, 0.021107485854707907, 0.01312597897770711, 0.006421229616742764, 0.001869516175091664, 0.0004650336886477315, 9.639585473975727e-05, 1.7127166183893358e-05, 2.6626906779063103e-06, 3.679623649786727e-07, 4.576448659535808e-08, 5.174413158105795e-09, 5.362966074594395e-10, 5.1308213178553486e-11, 4.558102088933874e-12], [0.004346223877381188, 0.005405517610160077, 0.0033614951114019644, 0.0013935944959573361, 0.000511309876373929, 0.00011909271481247176, 2.468647824420875e-05, 4.386178394549248e-06, 6.819012671099958e-07, 9.423325248017273e-08, 1.1720047565777047e-08, 1.3251403620932076e-09, 1.373427785689838e-10, 1.3139767179834798e-11, 1.1673062950386352e-12], [0.0008904363075204292, 0.001107460010533977, 0.0006886891653975925, 0.00028551385574476, 8.877534951690912e-05, 2.6057343434245464e-05, 5.057663193066279e-06, 8.986220231530361e-07, 1.3970510114283113e-07, 1.9306117621038064e-08, 2.401154697240879e-09, 2.714892569407951e-10, 2.8138218385393107e-11, 2.6920209587408816e-12, 2.391528684265228e-13], [0.00015202407885554406, 0.00018907650839127113, 0.00011757981464043158, 4.874574470234748e-05, 1.515660426400283e-05, 3.7701367242343257e-06, 9.221755433990451e-07, 1.5342162505655845e-07, 2.3851834357251022e-08, 3.296131034670058e-09, 4.09948839635936e-10, 4.635132671143193e-11, 4.804034487977544e-12, 4.596083999000812e-13, 4.0830539165058825e-14], [2.2247187320273888e-05, 2.7669435866412728e-05, 1.720661740614368e-05, 7.133447027755662e-06, 2.218015834984526e-06, 5.517214020206909e-07, 1.143651684260858e-07, 2.3977477071623276e-08, 3.4904748699850895e-09, 4.823554604803894e-10, 5.999186902343128e-11, 6.783048156945537e-12, 7.030218893721974e-13, 6.725904372204369e-14, 5.9751367022324615e-15], [2.8486946210471524e-06, 3.5429994805783266e-06, 2.203262720165489e-06, 9.134193857833791e-07, 2.840111735275325e-07, 7.064649421190681e-08, 1.4644163122303922e-08, 2.6019066493768753e-09, 4.773198269255085e-10, 6.176436535197434e-11, 7.681803193065848e-12, 8.685517194070475e-13, 9.002012910224958e-14, 8.612346060176129e-15, 7.651007535752382e-16], [3.2423818304788444e-07, 4.032639039771963e-07, 2.5077517817652125e-07, 1.039653179456104e-07, 3.232612797085781e-08, 8.040978051045504e-09, 1.6667974194044237e-09, 2.961487967931269e-10, 4.6041045671396356e-11, 7.507760666920805e-12, 8.743421957020924e-13, 9.885848391855251e-14, 1.0246083550759882e-14, 9.802565068573885e-16, 8.708370365673399e-17], [3.321428654110828e-08, 4.130951738156789e-08, 2.5688888788654364e-08, 1.0649991398677932e-08, 3.3114214590514182e-09, 8.237011031447376e-10, 1.7074326833956635e-10, 3.033686811043689e-11, 4.716349164084021e-12, 6.517613956744418e-13, 9.56525128692244e-14, 1.0126857919770138e-14, 1.0495875340160538e-15, 1.0041544211879213e-16, 8.920673867360526e-18], [3.0930932542600624e-09, 3.846964750891889e-09, 2.3922876838941263e-09, 9.917845597076985e-10, 3.0837740152350086e-10, 7.670748316421753e-11, 1.5900532767963714e-11, 2.8251325522718434e-12, 4.3921183633157765e-13, 6.069553154040055e-14, 7.548869406086658e-15, 1.0071565408696042e-15, 9.774324422722293e-17, 9.351226805873578e-18, 8.307411971181897e-19], [2.6404171124973783e-10, 3.2839590417907016e-10, 2.042174877809124e-10, 8.466362660602493e-11, 2.6324617499607602e-11, 6.54812947926643e-12, 1.3573479803925351e-12, 2.4116726276577964e-13, 3.74932908040861e-14, 5.181270235246631e-15, 6.444087624059481e-16, 7.286080162713378e-17, 8.910877011580772e-18, 7.982668885610263e-19, 7.09161700801084e-20], [2.0806065310038768e-11, 2.5877072972900415e-11, 1.6092012008674356e-11, 6.671358613047314e-12, 2.0743378323305313e-12, 5.159821490300342e-13, 1.0695685388050349e-13, 1.9003595288026957e-14, 2.954411458196705e-15, 4.0827582276021313e-16, 5.077838169401246e-17, 5.741314847645799e-18, 5.950525366003248e-19, 6.717686138702568e-20, 5.588080986299159e-21], [1.522378677887325e-12, 1.8934240353975207e-12, 1.1774516517783139e-12, 4.881429503224156e-13, 1.517791874445063e-13, 3.775438604793751e-14, 7.826027236539774e-15, 1.3904920434779878e-15, 2.1617412723849048e-16, 2.987351995704636e-17, 3.7154514530573e-18, 4.2009169811058304e-19, 4.3539962046837084e-20, 4.165526358758853e-21, 4.3666622509690935e-22]] |
| Legacy trial inputs | {"lambda_home": 1.0243792458028642, "lambda_away": 1.2437273740756227, "rho": 0.05, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2840 |
| Legacy p draw | 0.2923 |
| Legacy p away | 0.4238 |
| Legacy p over 1 5 | 0.6554 |
| Legacy p under 3 5 | 0.8058 |
| Legacy p btts yes | 0.4551 |
| Legacy p over 2 5 | 0.3895 |
| Legacy goal margin distribution | {"-1": 0.23937262928543895, "-10": 2.8665445980080805e-07, "-11": 3.210344615024921e-08, "-12": 3.3001831162063143e-09, "-13": 3.124510279971302e-10, "-14": 2.544210176744726e-11, "-2": 0.12129702132889415, "-3": 0.04571321294073203, "-4": 0.013394245397494845, "-5": 0.0031997843716445374, "-6": 0.0006441635755817052, "-7": 0.00011194873493698806, "-8": 1.7105703620338964e-05, "-9": 2.331243212813468e-06, "0": 0.2922708327222527, "1": 0.1794999271328928, "10": 3.727229191758158e-08, "11": 3.438069313398129e-09, "12": 2.9109623587441654e-10, "13": 2.269948934543629e-11, "14": 1.522378677887325e-12, "2": 0.07447198148304708, "3": 0.023116394512490628, "4": 0.005578689375341238, "5": 0.0010976660186773858, "6": 0.00018200413226557784, "7": 2.605192700430576e-05, "8": 3.2786660467983865e-06, "9": 3.6802676383217086e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3103 |
| Legacy raw p draw | 0.2706 |
| Legacy raw p away | 0.4191 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0244 |
| Legacy lambda away | 1.2437 |
| Legacy model home team | Maritimo |
| Legacy model away team | Santa Clara |
| Legacy home name match score | 95/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 57.3% |
| Market reference home draw last update utc | 2026-10-31T12:02:17Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 73.0% |
| Market reference draw away last update utc | 2026-10-31T12:02:17Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.7% |
| Market reference home away last update utc | 2026-10-31T12:02:17Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.28 |
| Market reference dc home draw odds | 1.63 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 65.6% |
| Market over 1 5 odds | 1.48 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference over 1 5 odds | 1.48 |
| Market reference over 1 5 opposite odds | 2.70 |
| Market reference over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 83.1% |
| Market under 3 5 odds | 1.18 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 3 5 odds | 1.18 |
| Market reference under 3 5 opposite odds | 4.91 |
| Market reference under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 46.4% |
| Market reference btts yes odds | 1.88 |
| Market reference btts yes opposite odds | 1.67 |
| Market reference btts yes last update utc | 2026-10-31T12:02:57Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,412.3721 |
| Elo away rating | 1,471.5616 |
| Elo rating diff | 0.8105 |
| Elo home expectancy | 0.5012 |

</details>


---

## 2026-11-02 — Benfica vs Alverca

The model's most likely 1X2 outcome is **Benfica win** at **82.6%**. Expected goals are 2.60 for Benfica and 0.73 for Alverca (3.33 combined). The most likely exact score is 2-0 at 12.9%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 66.0%; Under 3.5 goals: 56.3%; Double Chance 1X: 94.3%; Double Chance X2: 17.4%; Double Chance 12 (either team wins): 88.4%; Under 4.5 goals: 74.9%; BTTS Yes (both teams score): 46.6%; BTTS No (at least one team does not score): 53.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Benfica win | 82.6% | 1.21 |
| Draw | 11.6% | 8.60 |
| Alverca win | 5.7% | 17.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Benfica expected goals | 2.60 |
| Alverca expected goals | 0.73 |
| Expected total goals | 3.33 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 85.0% |
| Under 1.5 | 15.0% |
| Over 2.5 | 66.0% |
| Under 2.5 | 34.0% |
| Over 3.5 | 43.7% |
| Under 3.5 | 56.3% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.86% |
| 2 | 3-0 | 11.15% |
| 3 | 1-0 | 10.24% |
| 4 | 2-1 | 9.36% |
| 5 | 3-1 | 8.12% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T20:15:00+00:00 |
| Fixture id | cdf1a22ce6d16f0903216518d909e02a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 3.00 |
| Matched home-team name | Benfica |
| Matched away-team name | Alverca |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7756 |
| Dc lambda away | 0.6735 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 2.1976 |
| Shot lambda away | 0.8552 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 46.6% |
| P btts no | 53.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 36.22 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.67 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.94 |
| Fair Over 3.5 odds | 2.29 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.98 |
| Fair Under 4.5 odds | 1.34 |
| Goal margin distribution | {"-1": 0.042775426483004, "-10": 3.309127207475816e-10, "-11": 2.1595030305819744e-11, "-12": 1.294589961724327e-12, "-13": 7.175961108735264e-14, "-14": 3.698543262114457e-15, "-15": 1.7811351783644253e-16, "-16": 8.048740701266117e-18, "-17": 3.4252916391741097e-19, "-18": 1.3719389700021403e-20, "-19": 4.780262760420027e-22, "-2": 0.011551065915384207, "-3": 0.0024483355606518572, "-4": 0.00040907623240206387, "-5": 5.616545541472062e-05, "-6": 6.529876614619696e-06, "-7": 6.574516684347094e-07, "-8": 5.8326906985504206e-08, "-9": 4.622509626781542e-09, "0": 0.1163455441827971, "1": 0.23069490466270265, "10": 0.0001767697413911014, "11": 4.123289743741834e-05, "12": 8.835229657727664e-06, "13": 1.7504965357992559e-06, "14": 3.2248346687683806e-07, "15": 5.55097413886286e-08, "16": 8.965940053134975e-09, "17": 1.3638324536000286e-09, "18": 1.9525125332704717e-10, "19": 2.431679754938018e-11, "2": 0.23160714475763125, "3": 0.1754673845548321, "4": 0.10479131285773041, "5": 0.05142637239081557, "6": 0.02137062149972412, "7": 0.007690801120311566, "8": 0.002438777994375567, "9": 0.0006908387930744317} |
| Raw goal margin distribution | {"-1": 0.06326535278067999, "-10": 4.894237588964458e-10, "-11": 3.1939300737305376e-11, "-12": 1.9147135953713753e-12, "-13": 1.0613329858089436e-13, "-14": 5.470188458442359e-15, "-15": 2.634319624003694e-16, "-16": 1.1904181016363262e-17, "-17": 5.066046133173357e-19, "-18": 2.0291136773407732e-20, "-19": 7.070064165052404e-22, "-2": 0.017084160701940222, "-3": 0.0036211167416803705, "-4": 0.0006050285008237399, "-5": 8.306936115088647e-05, "-6": 9.657763384366741e-06, "-7": 9.723786566171368e-07, "-8": 8.626617313821549e-08, "-9": 6.836745447450325e-09, "0": 0.13652883684841244, "1": 0.21740565734790182, "10": 0.00016658686884541435, "11": 3.885766434610742e-05, "12": 8.326273674602353e-06, "13": 1.6496586719463424e-06, "14": 3.039067126458481e-07, "15": 5.2312086534601026e-08, "16": 8.449454459532471e-09, "17": 1.2852684870558094e-09, "18": 1.8400374789218846e-10, "19": 2.2916021329332607e-11, "2": 0.21826534758591137, "3": 0.16535953465481032, "4": 0.09875477869567272, "5": 0.048463941199698386, "6": 0.02013956061090186, "7": 0.007247770277102432, "8": 0.002298291476216284, "9": 0.0006510428227679019} |
| Unadjusted home-win probability | 77.9% |
| Unadjusted draw probability | 13.7% |
| Unadjusted away-win probability | 8.5% |
| Raw p over 1 5 | 84.2% |
| Raw p under 3 5 | 57.4% |
| Raw p btts yes | 47.5% |
| P home draw | 94.3% |
| P draw away | 17.4% |
| P home away | 88.4% |
| Raw p home draw | 91.5% |
| Raw p draw away | 22.1% |
| Raw p home away | 86.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6602 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 2.0, "market_key": "spreads", "opposite_price": 1.78, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -2.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.17 |
| Reference draw odds | 8.20 |
| Reference away odds | 18.50 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:35Z |
| Market reference home last update utc | 2026-10-31T12:02:35Z |
| Market reference draw last update utc | 2026-10-31T12:02:35Z |
| Market reference away last update utc | 2026-10-31T12:02:35Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 2.95 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:38Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:38Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.9% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | -0.0680 |
| Raw edge prob draw | 0.0288 |
| Raw edge prob away | 0.0392 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.02775265723410277, 0.020306299964640912, 0.0058578865250983455, 0.001283668148072082, 0.00021097249502632814, 2.7738878603154224e-05, 3.0392800179335566e-06, 2.854340238858768e-07, 2.345572267842333e-08, 1.713323509158653e-09, 1.1263476033345249e-10, 6.731515023051846e-12, 3.6877768911780417e-13, 1.864894857997398e-14, 8.757081287366841e-16, 3.837966567125378e-17, 1.576936733434871e-18, 6.098154365648718e-20, 2.227198748123742e-21, 7.706167385966784e-23], [0.09341341323423616, 0.05321662425256894, 0.01633691995664278, 0.003579991468952772, 0.00058837615743, 7.736029666760294e-05, 8.476175522701979e-06, 7.960401385630709e-07, 6.541510530816905e-08, 4.778247053614498e-09, 3.141243955510668e-10, 1.877336162920809e-11, 1.028475297891182e-12, 5.2009607717941766e-14, 2.442241505235108e-15, 1.0703613382532317e-16, 4.397881229080775e-18, 1.700699720419768e-19, 6.211381446147374e-21, 2.149154634826541e-22], [0.1261138260443113, 0.08290787172010017, 0.025675920202132992, 0.00499207639335106, 0.0008204541131982397, 0.00010787414275317925, 1.1819501833941057e-05, 1.1100286741864961e-06, 9.121731317226007e-08, 6.662969597781148e-09, 4.38027015764053e-10, 2.6178290151184888e-11, 1.4341451090801467e-12, 7.252417698976682e-14, 3.40555453019354e-15, 1.492552598348132e-16, 6.132573011655271e-18, 2.3715204352064543e-19, 8.661386753662156e-21, 2.9968630403795317e-22], [0.11723861343076548, 0.07707326173376981, 0.02533417745421472, 0.005230531232684645, 0.0007627149665662595, 0.00010028254092435153, 1.0987708881076687e-05, 1.0319108277968704e-06, 8.479792939941547e-08, 6.194065642737221e-09, 4.0720103087943773e-10, 2.4336002923540054e-11, 1.3332176916747714e-12, 6.742031557666174e-14, 3.165889923460636e-15, 1.3875147760669688e-16, 5.700995514930927e-18, 2.204625585212524e-19, 8.051844950213175e-21, 2.7859599420332793e-22], [0.0817409929007649, 0.053736945157060595, 0.01766347075278748, 0.00387068521942313, 0.0005993604874878809, 6.99188963933703e-05, 7.66083978103473e-06, 7.194678713850402e-07, 5.91227304912687e-08, 4.3186204690901815e-09, 2.839083097307059e-10, 1.696752446992065e-11, 9.295447522050254e-13, 4.700672735415559e-14, 2.2073187168067427e-15, 9.674017129789249e-17, 3.974842590478586e-18, 1.5371069226788702e-19, 5.6138995647718946e-21, 1.9424243018537616e-22], [0.0455931009409194, 0.029973136829606423, 0.009852246423976106, 0.0021589723302471915, 0.0003548298521616655, 4.3955213324955264e-05, 4.2730266544836515e-06, 4.013013559014353e-07, 3.2977194471612083e-08, 2.408819516197813e-09, 1.5835702215206096e-10, 9.464064827470099e-12, 5.184770359694156e-13, 2.62191880610278e-14, 1.231187700231725e-15, 5.3959271089125366e-17, 2.2170687316211924e-18, 8.573601640460122e-20, 3.131294108937027e-21, 1.0834361575718602e-22], [0.021192251888560602, 0.013931894354069416, 0.004579449161741129, 0.001003517736210124, 0.00016492941803486588, 2.1685087927632897e-05, 2.238567443012181e-06, 1.8652996269116293e-07, 1.532821846722055e-08, 1.1196498787721044e-09, 7.360635342872498e-11, 4.399017429705204e-12, 2.409947057326998e-13, 1.218701132925479e-14, 5.722716666984005e-16, 2.5080953939186286e-17, 1.0305216808054295e-18, 3.985118840507263e-20, 1.4554652375970029e-21, 5.035948747199666e-23], [0.008443223661470236, 0.005550618248496671, 0.0018245023569101666, 0.0003998123814132269, 6.570967408971648e-05, 8.639574900036186e-06, 9.466167588380608e-07, 8.375994723390309e-08, 6.106928963055653e-09, 4.46080690184407e-10, 2.9325571825588697e-11, 1.7526163923030684e-12, 9.601491207405575e-14, 4.855437872240144e-15, 2.279992566370504e-16, 9.992524856024918e-18, 4.105710466631046e-19, 1.5877146923732186e-20, 5.798731818188618e-22, 2.006376757123171e-23], [0.0029433881260433744, 0.0019349983489576146, 0.0006360388861631087, 0.00013937840134059618, 2.2907017773845485e-05, 3.0118380365634857e-06, 3.299996114745153e-07, 3.09919179635149e-08, 2.3994887217365996e-09, 1.5550797413287795e-10, 1.0223173442007268e-11, 6.109787547325904e-13, 3.347171216268159e-14, 1.6926518534751629e-15, 7.948271082698663e-17, 3.483489267805974e-18, 1.4312897444137453e-19, 5.5349245269930174e-21, 2.021493100751782e-22, 6.994420330513199e-24], [0.0009120827681617771, 0.0005996078583350655, 0.00019709263036608206, 4.3189899759356704e-05, 7.098315032474292e-06, 9.332936928492845e-07, 1.0225867138038168e-07, 9.603624502217219e-09, 7.891839590986623e-10, 5.4312023798145865e-11, 3.1679071644955554e-12, 1.8932711896668314e-13, 1.0372051043601638e-14, 5.245107073687499e-16, 2.4629715079244607e-17, 1.0794466778369732e-18, 4.4352109073746186e-20, 1.7151354384691544e-21, 6.264104304966708e-23, 2.1673968853428342e-24], [0.0002543685869203817, 0.00016722320490545015, 5.496669340621623e-05, 1.2045128089813745e-05, 1.9796321423385663e-06, 2.6028405109575456e-07, 2.8518676865047073e-08, 2.678331922514356e-09, 2.200936313057862e-10, 1.607674160810159e-11, 9.957682571650214e-13, 5.28009884610825e-14, 2.892636567122444e-15, 1.462795396594249e-16, 6.868922470255279e-18, 3.0104430834789024e-19, 1.2369253872392419e-20, 4.783300300034671e-22, 1.746981103028185e-23, 6.044601457951298e-25], [6.449113478660976e-05, 4.239680055455042e-05, 1.3935936336132968e-05, 3.053851847694149e-06, 5.019044405802446e-07, 6.59909072313053e-08, 7.230459766697517e-09, 6.790487265324851e-10, 5.580126152392651e-11, 4.0760037335195844e-12, 2.6795856193479894e-13, 1.5088122429202566e-14, 7.333822819771386e-16, 3.7086865256880135e-17, 1.741506725461589e-18, 7.632502622064087e-20, 3.1360288168913695e-21, 1.2127301885390524e-22, 4.4291944673308e-24, 1.53251316161178e-25], [1.4988148916959697e-05, 9.853285454145537e-06, 3.2388000272341144e-06, 7.097345459189523e-07, 1.166457765457396e-07, 1.5336705549077086e-08, 1.6804047266330483e-09, 1.5781523257137526e-10, 1.296856723396463e-11, 9.472891296798777e-13, 6.227526997535506e-14, 3.7218254308231314e-15, 1.921033768878269e-16, 8.619222799732029e-18, 4.047372127575693e-19, 1.7738420371590988e-20, 7.288329949685429e-22, 2.818461905199707e-23, 1.0293728971925542e-24, 3.561657824666969e-26], [3.215391606689279e-06, 2.1138148228380266e-06, 6.948163166119672e-07, 1.5225859541220377e-07, 2.502389407383901e-08, 3.2901670893439768e-09, 3.6049543434566517e-10, 3.385593357986524e-11, 2.7821329015280425e-12, 2.0322092698412583e-13, 1.3359847269497474e-14, 7.98439241438956e-16, 4.3741502076502584e-17, 2.084061767387651e-18, 8.682784271931856e-20, 3.805404409493243e-21, 1.5635576532391646e-22, 6.04641627459284e-24, 2.2083027011035044e-25, 7.640786556620629e-27], [6.405234950313621e-07, 4.2108340873832223e-07, 1.3841118904311488e-07, 3.0330740267872845e-08, 4.984895792513917e-09, 6.554191778443056e-10, 7.181265108410419e-11, 6.744286095357879e-12, 5.542160046761274e-13, 4.048271387677486e-14, 2.6613542339107868e-15, 1.590534392242353e-16, 8.713545102772454e-18, 4.406406877802694e-19, 1.9494711250881215e-20, 7.580572541476789e-22, 3.114691879683581e-23, 1.2044790054684529e-24, 4.3990590796323547e-26, 1.5220862366666727e-27], [1.1908937946410355e-07, 7.828996475269176e-08, 2.5734110835741015e-08, 5.639245188048903e-09, 9.268171288465167e-10, 1.2185886042248852e-10, 1.3351772607278695e-11, 1.2539319045357205e-12, 1.0304265276439719e-13, 7.526751652368222e-15, 4.948124880806784e-16, 2.957202276852975e-17, 1.6200665350626073e-18, 8.192615334402168e-20, 3.847047898267514e-21, 1.5885342416889405e-22, 5.7909932430384655e-24, 2.239428505768634e-25, 8.17895393507301e-27, 2.829939991609698e-28], [2.0757845552055298e-08, 1.3646313415396398e-08, 4.485577979762678e-09, 9.829472717923974e-10, 1.615486360090939e-10, 2.1240579262250182e-11, 2.3272775026222622e-12, 2.1856629805509048e-13, 1.796082472662602e-14, 1.311948630613453e-15, 8.624817134010618e-17, 5.154544293146083e-18, 2.823853064833511e-19, 1.4280118390421255e-20, 6.705587556417379e-22, 2.9388582805082464e-23, 1.13767681418804e-24, 3.903430453395486e-26, 1.4256305921284568e-27, 4.9327200739277913e-29], [3.4053564802144866e-09, 2.2386986984570184e-09, 7.35865964634264e-10, 1.6125401132373136e-10, 2.6502302135536855e-11, 3.484549687626484e-12, 3.817934527423732e-13, 3.5856137264914675e-14, 2.9465009130852006e-15, 2.1522719011297816e-16, 1.4149145124099794e-17, 8.456109169518137e-19, 4.632574372609783e-20, 2.3426753791525433e-21, 1.1000619491857902e-22, 4.821242197251945e-24, 1.9809432387336576e-25, 7.217442894912974e-27, 2.3387689069764603e-28, 8.092203127106753e-30], [5.276176351956089e-10, 3.468585212908409e-10, 1.1401327947223065e-10, 2.4984303586059296e-11, 4.106202114590589e-12, 5.398876377815471e-13, 5.915414724992598e-14, 5.555462537000488e-15, 4.565236717202065e-16, 3.3346776390955944e-17, 2.1922340682367592e-18, 1.3101689496824866e-19, 7.177597850754834e-21, 3.6296841483731814e-22, 1.704409178805038e-23, 7.469915180977273e-25, 3.0692251843529525e-26, 1.1868966306817253e-27, 4.0841401620193085e-29, 1.2537862342029035e-30], [7.744527544616522e-11, 5.091291861815749e-11, 1.6735206036041542e-11, 3.667269901499076e-12, 6.027204789775398e-13, 7.924630267991348e-14, 8.682820516139682e-15, 8.154472059095334e-16, 6.700989342586771e-17, 4.894738368405385e-18, 3.2178259393115183e-19, 1.9231046959140317e-20, 1.0535490201866134e-21, 5.327757639282186e-23, 2.501782152838606e-24, 1.0964562216268599e-25, 4.505099412008811e-27, 1.7421619437567401e-28, 6.362811873082307e-30, 2.0742243487603545e-31]] |
| Legacy trial inputs | {"lambda_home": 2.7888761393117814, "lambda_away": 0.657405094434053, "rho": 0.05, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8323 |
| Legacy p draw | 0.1125 |
| Legacy p away | 0.0552 |
| Legacy p over 1 5 | 0.8585 |
| Legacy p under 3 5 | 0.5444 |
| Legacy p btts yes | 0.4466 |
| Legacy p over 2 5 | 0.6733 |
| Legacy goal margin distribution | {"-1": 0.04247239599986994, "-10": 1.3291194971190844e-10, "-11": 7.835779385534342e-12, "-12": 4.2433566489768207e-13, "-13": 2.12463032329047e-14, "-14": 9.891030203753642e-16, "-15": 4.30229450312356e-17, "-16": 1.7559466882247134e-18, "-17": 6.74926114066725e-20, "-18": 2.442114211606396e-21, "-19": 7.706167385966784e-23, "-2": 0.010366692574025234, "-3": 0.0019916597517991436, "-4": 0.0003012458112986494, "-5": 3.741436220368327e-05, "-6": 3.933025153616901e-06, "-7": 3.5793679824275124e-07, "-8": 2.869728909707474e-08, "-9": 2.055007675964757e-09, "0": 0.11252137340450422, "1": 0.2059036409822727, "10": 0.0003001615552158264, "11": 7.507051574275917e-05, "12": 1.724617926718418e-05, "13": 3.6632191244077285e-06, "14": 7.234644772235575e-07, "15": 1.3349714586819926e-07, "16": 2.3114224799886048e-08, "17": 3.768950207541369e-09, "18": 5.785305538137664e-10, "19": 7.744527544616522e-11, "2": 0.22318343968151938, "3": 0.181900149253904, "4": 0.11671726079589244, "5": 0.06149624204342127, "6": 0.0274241462608518, "7": 0.010587877377373964, "8": 0.0036011365386607467, "9": 0.00109397733683585} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.8178 |
| Legacy raw p draw | 0.1173 |
| Legacy raw p away | 0.0649 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.7889 |
| Legacy lambda away | 0.6574 |
| Legacy model home team | Benfica |
| Legacy model away team | Alverca |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,677.3736 |
| Elo away rating | 1,429.6982 |
| Elo rating diff | 307.6754 |
| Elo home expectancy | 0.8546 |

</details>


---

## 2026-11-02 — Gil Vicente vs Vitória SC

The model's most likely 1X2 outcome is **Vitória SC win** at **35.0%**. Expected goals are 1.20 for Gil Vicente and 1.08 for Vitória SC (2.28 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 38.9%; Under 3.5 goals: 80.5%; Double Chance 1X: 65.0%; Double Chance X2: 65.0%; Double Chance 12 (either team wins): 70.0%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 46.2%; BTTS No (at least one team does not score): 53.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Gil Vicente win | 35.0% | 2.86 |
| Draw | 30.0% | 3.33 |
| Vitória SC win | 35.0% | 2.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Gil Vicente expected goals | 1.20 |
| Vitória SC expected goals | 1.08 |
| Expected total goals | 2.28 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
| Over 1.5 | 65.7% |
| Under 1.5 | 34.3% |
| Over 2.5 | 38.9% |
| Under 2.5 | 61.1% |
| Over 3.5 | 19.5% |
| Under 3.5 | 80.5% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.94% |
| 2 | 0-1 | 12.25% |
| 3 | 1-0 | 11.49% |
| 4 | 0-0 | 10.60% |
| 5 | 1-2 | 7.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Gil Vicente win | 35.0% | 33.1% | 2.89 | +1.0% |
| Draw | 30.0% | 31.3% | 3.05 | -8.4% |
| Vitória SC win | 35.0% | 35.6% | 2.69 | -5.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T20:15:00+00:00 |
| Fixture id | 97ce048d06fc45fc59e114548540828f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:35Z |
| Market best draw last update utc | 2026-10-31T12:02:35Z |
| Market best away last update utc | 2026-10-31T12:02:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Gil Vicente |
| Matched away-team name | Guimaraes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1706 |
| Dc lambda away | 1.0202 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.2631 |
| Shot lambda away | 1.2218 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.2% |
| P btts no | 53.8% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.44 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.91 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.12 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.67 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.21533751556046818, "-10": 7.197611570047501e-08, "-11": 7.0019349207238004e-09, "-12": 6.228172023980797e-10, "-13": 4.708350215224065e-11, "-2": 0.09416355571542573, "-3": 0.03079136825466239, "-4": 0.007832077576880711, "-5": 0.001624694126792689, "-6": 0.0002840616647672972, "-7": 4.287942514346135e-05, "-8": 5.691368383549067e-06, "-9": 6.738024830433392e-07, "0": 0.3003146338497271, "1": 0.20247472245789552, "10": 1.720851091058482e-07, "11": 1.8563254407211087e-08, "12": 1.8309555748935742e-09, "13": 1.5348542014600216e-10, "2": 0.09848916349583484, "3": 0.035712129509401454, "4": 0.010072676855677823, "5": 0.002316971502780097, "6": 0.0004492032301471912, "7": 7.519004726980363e-05, "8": 1.1066473827407518e-05, "9": 1.4528016759225672e-06} |
| Raw goal margin distribution | {"-1": 0.20616423021940677, "-10": 6.890996419713277e-08, "-11": 6.703655511303823e-09, "-12": 5.962854580429496e-10, "-13": 4.507776525602528e-11, "-2": 0.09015222883140223, "-3": 0.02947966923971577, "-4": 0.007498434448143672, "-5": 0.001555482857320088, "-6": 0.0002719607602937541, "-7": 4.10527801156413e-05, "-8": 5.4489185436895065e-06, "-9": 6.450987877100633e-07, "0": 0.27134846736796037, "1": 0.2278878407155002, "10": 1.9368394956846022e-07, "11": 2.089317576119421e-08, "12": 2.0607634737974338e-09, "13": 1.7274976626110605e-10, "2": 0.11085078932561067, "3": 0.040194449867400915, "4": 0.011336924189846708, "5": 0.002607780499008725, "6": 0.0005055838719915206, "7": 8.462734166322976e-05, "8": 1.245545515138033e-05, "9": 1.6351465155493708e-06} |
| Unadjusted home-win probability | 39.3% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 33.5% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 45.5% |
| P home draw | 65.0% |
| P draw away | 65.0% |
| P home away | 70.0% |
| Raw p home draw | 66.5% |
| Raw p draw away | 60.7% |
| Raw p home away | 72.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.3895 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.89 |
| Reference draw odds | 3.05 |
| Reference away odds | 2.69 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:35Z |
| Market reference home last update utc | 2026-10-31T12:02:35Z |
| Market reference draw last update utc | 2026-10-31T12:02:35Z |
| Market reference away last update utc | 2026-10-31T12:02:35Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.24 |
| Reference Under 2.5 odds | 1.64 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:35Z |
| Home probability edge | +1.9% |
| Draw probability edge | -1.2% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -2.7% |
| Under 2.5 probability edge | +2.7% |
| Raw edge prob home | 0.0627 |
| Raw ev home | 0.1372 |
| Raw edge prob draw | -0.0414 |
| Raw ev draw | -0.1724 |
| Raw edge prob away | -0.0213 |
| Raw ev away | -0.0984 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.10875202709757463, 0.12515679089740614, 0.06217106471515958, 0.021791863026958284, 0.0057287738640325655, 0.0012048111699168851, 0.0002111519250029519, 3.1719352646199086e-05, 4.169285530998061e-06, 4.871317529467731e-07, 5.122403075257146e-08, 4.896754990574561e-09, 4.290959730224622e-10, 3.470870391988794e-11], [0.12322062261548727, 0.13527506573803058, 0.07265700834081695, 0.025467338881291098, 0.006695004699190471, 0.0014080179521264592, 0.00024676539233175094, 3.706922634088729e-05, 4.872488753230387e-06, 5.69292740909104e-07, 5.986361737074035e-08, 5.722655222701372e-09, 5.014684859225509e-10, 4.056276986344308e-11], [0.06840512778411703, 0.07193097859153644, 0.043747241546029415, 0.014881365326410347, 0.003912101348911587, 0.0008227490759598257, 0.00014419276275078163, 2.1660712260415452e-05, 2.847148087345477e-06, 3.326556141036577e-07, 3.498019027456664e-08, 3.3439270354497263e-09, 2.930237734488034e-10, 2.3702099375307902e-11], [0.026647508572978457, 0.028021018756517167, 0.014732662342574225, 0.005973442418799708, 0.001523975725364954, 0.00032050540310722345, 5.617090422942041e-05, 8.438022621313796e-06, 1.109118651243773e-06, 1.2958740983062482e-07, 1.3626681952377907e-08, 1.3026410041331846e-09, 1.141486576811352e-10, 9.233253657451047e-12], [0.007785487756721606, 0.008186780308645827, 0.00430437847417886, 0.0015087473015822652, 0.00045879768304727016, 9.364068258091217e-05, 1.6411211050536665e-05, 2.4653007101682573e-06, 3.240464171861159e-07, 3.786099514326292e-08, 3.981248949200337e-09, 3.8058700914975955e-10, 3.335032145271026e-11, 2.6976399353778425e-12], [0.001819721928421532, 0.0019135170610152846, 0.0010060733691253263, 0.0003526433583773518, 9.27049721401826e-05, 2.2552657495538026e-05, 3.835834253908159e-06, 5.762210284863942e-07, 7.574019632500368e-08, 8.84934704759825e-09, 9.305474803566754e-10, 8.895557322330376e-11, 7.795055770912826e-12, 6.305262687176607e-13], [0.0003544402098120838, 0.00037270935629905237, 0.00019596008075170444, 6.868686032735038e-05, 1.805680816546064e-05, 3.7975044376214405e-06, 7.698599739069438e-07, 1.1223467665304836e-07, 1.4752457865872401e-08, 1.7236503969435567e-09, 1.8124936509603e-10, 1.7326511015104e-11, 1.5182985706699824e-12, 1.2281209534589326e-13], [5.917443933265736e-05, 6.22245066515592e-05, 3.271589280519899e-05, 1.1467396578809197e-05, 3.0146170489374727e-06, 6.340002904260382e-07, 1.1111316455102562e-07, 1.9307772707898836e-08, 2.4629497410987268e-09, 2.877665767626176e-10, 3.0259912002207695e-11, 2.892692608024002e-12, 2.5348271491714993e-13, 2.050370325989557e-14], [8.64437047976856e-06, 9.089932992741474e-06, 4.7792307147126225e-06, 1.6751899229394124e-06, 4.403838366620625e-07, 9.261656648597811e-08, 1.6231727252352134e-08, 2.4383385601011206e-09, 3.707393811693963e-10, 4.203776037904903e-11, 4.420454050469022e-12, 4.225727673949806e-13, 3.7029476285246626e-14, 2.9952393159044107e-15], [1.1224837665903754e-06, 1.180340690814509e-06, 6.205898864018453e-07, 2.1752578731512398e-07, 5.718446576056365e-08, 1.2026392510728207e-08, 2.1077128042036057e-09, 3.166217201785337e-10, 4.1617695400800124e-11, 5.624711073920476e-12, 5.740022277183792e-13, 5.487167315586129e-14, 4.8083300123255996e-15, 3.8893607313854704e-16], [1.3118049813887457e-07, 1.3794202143783438e-07, 7.252602920524026e-08, 2.542142878798718e-08, 6.6829355822779154e-09, 1.405479711446621e-09, 2.4632054718169676e-10, 3.70024014697083e-11, 4.863705094508688e-12, 5.682664741690176e-13, 6.912207005872033e-14, 6.412648122443783e-15, 5.619316243200104e-16, 4.545351063158068e-17], [1.393688759626569e-08, 1.4655245824310933e-08, 7.705315433143451e-09, 2.7008252032979333e-09, 7.100089063901063e-10, 1.4932107314096791e-10, 2.6169604685352505e-11, 3.93121170746947e-12, 5.167300945281647e-13, 6.037380622564364e-14, 6.348569330667455e-15, 7.02017409716006e-16, 5.970077866790889e-17, 4.829075034136337e-18], [1.3572934651704571e-09, 1.427253341207521e-09, 7.50409602735473e-10, 2.630294873000332e-10, 6.914674759336722e-11, 1.4542164840360808e-11, 2.548620212380881e-12, 3.8285506171260264e-13, 5.032360171634837e-14, 5.8797182722123876e-15, 6.182780485368457e-16, 5.910421486273833e-17, 5.991035699818478e-18, 4.702966814776699e-19], [1.220167948294636e-10, 1.2830598729944803e-10, 6.745967389118352e-11, 2.364559751413567e-11, 6.216094551936134e-12, 1.3072989660933096e-12, 2.291136570920187e-13, 3.4417573437990104e-14, 4.523947652641342e-15, 5.28569831422189e-16, 5.558142563252317e-17, 5.313299624232396e-18, 4.655972121554664e-19, 4.356439828666471e-20]] |
| Legacy trial inputs | {"lambda_home": 1.1686627641604554, "lambda_away": 1.0515436623193923, "rho": 0.05, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3611 |
| Legacy p draw | 0.2942 |
| Legacy p away | 0.3446 |
| Legacy p over 1 5 | 0.6429 |
| Legacy p under 3 5 | 0.8160 |
| Legacy p btts yes | 0.4466 |
| Legacy p over 2 5 | 0.3770 |
| Legacy goal margin distribution | {"-1": 0.21431673154707784, "-10": 5.724894300237909e-08, "-11": 5.4219255758724195e-09, "-12": 4.696587428859053e-10, "-13": 3.470870391988794e-11, "-2": 0.09188801282524883, "-3": 0.02936833050158223, "-4": 0.00728975568147483, "-5": 0.001474385202285908, "-6": 0.00025120195858434, "-7": 3.693851220036253e-05, "-8": 4.774895084033586e-06, "-9": 5.504561436505798e-07, "0": 0.29422991668515763, "1": 0.21148962692145348, "10": 1.4660979916343509e-07, "11": 1.5431600611364397e-08, "12": 1.4855994524699052e-09, "13": 1.220167948294636e-10, "2": 0.10110187573491997, "3": 0.03591215848993026, "4": 0.00990688495559919, "5": 0.002226880983951179, "6": 0.0004216683078053639, "7": 6.891110842077354e-05, "8": 9.900008479038166e-06, "9": 1.2684003490432051e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3915 |
| Legacy raw p draw | 0.2757 |
| Legacy raw p away | 0.3328 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1687 |
| Legacy lambda away | 1.0515 |
| Legacy model home team | Gil Vicente |
| Legacy model away team | Guimaraes |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,467.0612 |
| Elo away rating | 1,413.2222 |
| Elo rating diff | 113.8391 |
| Elo home expectancy | 0.6582 |

</details>


---
