# Ligue 1 — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,761 |
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
| Training sha256 | d64703b08d0b253f68ae6aa61e0d2f2d7176bb4a80991112dca66465573aba1b |
| Training as of utc | 2026-11-05T16:26:08.120854+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 81, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 81, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 144, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_CHRONOLOGICAL_PARTITIONS', 'cutoff_utc': '2026-11-05T16:26:08.120854+00:00', 'observations': 519, 'observations_sha256': '09b43855723986c152174c7192f211cb1392e9bbac8dd5825656ed47f8834ff7', 'eligible_training_matches': 186, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 183, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 23, 'retrospective_eligible_training_matches': 186, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '06a1f681686c8f3d51c6b57bb667afee75b8eb0993b69eaa4c9987b68b43cf8a', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 126, 'tuning_matches': 17, 'audit_matches': 43, 'tuning_origin_utc': '2025-09-13T00:00:00+00:00', 'audit_origin_utc': '2025-10-05T00:00:00+00:00', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1759, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1471, 'tuning_matches': 187, 'audit_matches': 96, 'audit_matchdays': 34, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8547734904983413, 'audit_candidate_poisson_score': 0.8530374480014693, 'audit_gain': 0.0017360424968719812, 'audit_gain_lower95': -0.004922765199428151, 'audit_baseline_briers': [0.5824614078047651, 0.17370432402916056, 0.21287468772376236, 0.2466063615696182], 'audit_candidate_briers': [0.5816260245758471, 0.17326240897441395, 0.21186772195909942, 0.24573349270218828], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1597.008 |
| Base scoring parameter | 0.200 |
| Home-advantage parameter | 0.202 |
| Dixon-Coles low-score adjustment | -0.054 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1761, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261105T162608120854Z_5e9f6461fe81811891a12ebd0f9ce558ee4cf711751f404aaacc0d68336bc853.json |
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

## 2026-11-06 — Toulouse FC vs RC Strasbourg Alsace

The model's most likely 1X2 outcome is **Toulouse FC win** at **39.6%**. Expected goals are 1.50 for Toulouse FC and 1.39 for RC Strasbourg Alsace (2.89 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 55.2%; Under 3.5 goals: 67.1%; Double Chance 1X: 65.6%; Double Chance X2: 60.4%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse FC win | 39.6% | 2.53 |
| Draw | 26.0% | 3.84 |
| RC Strasbourg Alsace win | 34.4% | 2.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse FC expected goals | 1.50 |
| RC Strasbourg Alsace expected goals | 1.39 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 55.2% |
| Under 2.5 | 44.8% |
| Over 3.5 | 32.9% |
| Under 3.5 | 67.1% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.20% |
| 2 | 2-1 | 8.71% |
| 3 | 1-2 | 8.04% |
| 4 | 1-0 | 7.71% |
| 5 | 0-1 | 7.07% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:45:00+00:00 |
| Fixture id | fdorg:559638 |
| Matched home-team name | Toulouse |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.5044 |
| Dc lambda away | 1.3886 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_CHRONOLOGICAL_PARTITIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T16:26:08.120854+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.22 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.77 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.04 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.98 |
| Fair Under 4.5 odds | 1.20 |
| Score matrix json | [[0.061665132659574295,0.07068842495530818,0.05342419429850703,0.024729140208958122,0.008585020094885152,0.002384314841739082,0.0005518291552907256,0.00010947095143816804,1.900208236035687e-05,2.9319123112763357e-06,4.0713952682641977e-07,5.139760386759012e-08,5.947766593092302e-09,6.353351090428808e-10,6.301836193518451e-11,5.8340230620103006e-12],[0.07709981217935141,0.12200729027643441,0.08036910166602548,0.03720147415723767,0.01291494166398646,0.0035868625523641593,0.0008301484761011487,0.0001646834761129291,2.858593019770423e-05,4.410645059132404e-06,6.124835096424553e-07,7.732038460971029e-08,8.947568873666358e-09,9.55771306261695e-10,9.480216227307277e-11,8.776457909178915e-12],[0.06269828561081105,0.0870658724622662,0.0604519411796206,0.027982163305667357,0.009714346404590722,0.00269796227082334,0.0006244201541054762,0.0001238714332356749,2.1501733067235058e-05,3.317594077221967e-06,4.6069716260179697e-07,5.815876058731367e-08,6.730172367723965e-09,7.189109942699011e-10,7.13081845962116e-11,6.601466313457394e-12],[0.03144021765610163,0.04365940717460432,0.030313782424912124,0.014031728240222637,0.0048712841566825385,0.0013529001661890694,0.0003131171030065225,6.211565092030753e-05,1.0782099718221037e-05,1.6636161398401432e-06,2.3101778501023952e-07,2.916386107946394e-08,3.3748623593598944e-09,3.604997794598827e-10,3.5757673794828424e-11,3.310322375205985e-12],[0.011824333910805533,0.016419842077020495,0.011400693513395775,0.005277184842448848,0.0018320385397157914,0.000508811468418676,0.0001177600365121736,2.336104048650601e-05,4.055033865298495e-06,6.256684655316821e-07,8.688334982838858e-08,1.0968220236382593e-08,1.2692501011466716e-09,1.3558016085420282e-10,1.344808358035196e-11,1.2449772945274143e-12],[0.003557605712874998,0.004940263393976992,0.0034301443683799563,0.0015877548016668263,0.0005512082815205319,0.000153086896942957,3.5430645125915306e-05,7.028672542607186e-06,1.2200443385571413e-06,1.8824584320197092e-07,2.6140728436358487e-08,3.300025461676732e-09,3.8188124971505904e-10,4.0792213620307317e-11,4.0461457984504165e-12,3.7457825267966003e-13],[0.0008919852979847179,0.0012386539350473535,0.0008600273873766131,0.00039809187813197474,0.00013820240997038547,3.838291042007253e-05,8.883394367188212e-06,1.762273022461487e-06,3.0589719623623103e-07,4.7198182737119525e-08,6.554167978609298e-09,8.274031560434206e-10,9.574767071266846e-11,1.0227680568952519e-11,1.014475143397438e-12,9.391661732661528e-14],[0.0001916950016471073,0.0002661969526353857,0.0001848269829247138,8.555322986446393e-05,2.9700838418259593e-05,8.248804204307227e-06,1.9091147597358975e-06,3.7872701568809407e-07,6.573983188829918e-08,1.014327897329044e-08,1.4085447868855488e-09,1.778157663796861e-10,2.0576964593968145e-11,2.198012958219218e-12,2.1801908027395885e-13,2.0183456110534128e-14],[3.604723309012974e-05,5.005693167313095e-05,3.4755738426073484e-05,1.6087833235292484e-05,5.585085872015692e-06,1.5511440846793294e-06,3.58998952235046e-07,7.121761597712457e-08,1.236202834201141e-08,1.9073900639387378e-09,2.6486941137996375e-10,3.3437316167420915e-11,3.869389564844241e-12,4.133247333486192e-13,4.0997337109492103e-14,3.795392371889766e-15],[6.025326121827738e-06,8.367059331143151e-06,5.80945167409738e-06,2.68909520999431e-06,9.335519237542148e-07,2.592750724797253e-07,6.000698470260387e-08,1.1904085975429877e-08,2.066323706500829e-09,3.1882189537347913e-10,4.427315070952896e-11,5.5890762556902006e-12,6.467718052670034e-13,6.908758590197683e-14,6.8527402808854926e-15,6.344031106008764e-16],[9.064246153164073e-07,1.2587050696038345e-06,8.739493750913561e-07,4.0453612667340556e-07,1.4043960878753549e-07,3.900424692070926e-08,9.027197354233151e-09,1.7908004202267727e-09,3.1084901180685564e-10,4.796221947579681e-11,6.660265816210606e-12,8.407970278464028e-13,9.72976189061128e-14,1.0393244649028633e-14,1.0308973070291953e-15,9.543692471661563e-17],[1.2396244642865874e-07,1.7214024986046978e-07,1.1952113916644317e-07,5.532427858184781e-08,1.9206492395078644e-08,5.33421289282928e-09,1.2345576780639767e-09,2.449095020210696e-10,4.251164776682268e-11,6.559303401411517e-12,9.108566013009617e-13,1.14987230885607e-13,1.330640261471145e-14,1.4213780288561799e-15,1.4098530648513605e-16,1.3051934454990144e-17],[1.5540322430394512e-08,2.1580043498253492e-08,1.4983546173909418e-08,6.935625684716382e-09,2.4077863350996123e-09,6.687137165741669e-10,1.5476803603641952e-10,3.070262597523954e-11,5.329393960645904e-12,8.222949184484025e-13,1.1418785027138482e-13,1.4415161162287536e-14,1.6681325109235174e-15,1.7818842319004908e-16,1.7674361742997026e-17,1.6362315815350832e-18],[1.7983234429079916e-09,2.4972389276802315e-09,1.7338933901226398e-09,8.025894131814116e-10,2.7862862120893765e-10,7.738343644385542e-11,1.790973055184264e-11,3.5529026052973234e-12,6.167165539099111e-13,9.515582675026499e-14,1.3213798423942093e-14,1.6681199741864294e-15,1.9303600769592123e-16,2.0619933731281045e-17,2.0452741056841e-18,1.8934443762543346e-19],[1.9323727427410112e-10,2.6833862701349234e-10,1.8631399924775493e-10,8.624154413159216e-11,2.9939795040485845e-11,8.315169549362777e-12,1.9244744478364303e-12,3.817740451065975e-13,6.62687384448256e-14,1.022488622112712e-14,1.4198771640995753e-15,1.792463743077956e-16,2.0742515541917846e-17,2.215696962445263e-18,2.1977314196977656e-19,2.034584110549979e-20],[1.9379866301805085e-11,2.6911819858082165e-11,1.8685527464304735e-11,8.649209119772208e-12,3.0026775484579924e-12,8.339326599841684e-13,1.9300653893206373e-13,3.828831667937054e-14,6.646126094845968e-15,1.0254591339118824e-15,1.424002160484e-16,1.7976711699218816e-17,2.0802776248813958e-18,2.222133957271406e-19,2.204116221418229e-20,2.040494940241468e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.18445704616259992, "-10": 4.915644062451468e-07, "-11": 6.110108638661574e-08, "-12": 6.9781564063254145e-09, "-13": 7.367387376294111e-10, "-14": 7.179481984436342e-11, "-15": 5.8340230620103006e-12, "-2": 0.10181802004661171, "-3": 0.04067979097242165, "-4": 0.012862668467906862, "-5": 0.0033497695083884883, "-6": 0.0007397682619733353, "-7": 0.00014161685404908564, "-8": 2.3903899520143902e-05, "-9": 3.6060691640887348e-06, "0": 0.26015049260152073, "1": 0.2003482255485063, "10": 1.0943817744916683e-06, "11": 1.4736562753871493e-07, "12": 1.823252456644227e-08, "13": 2.085347597385789e-09, "14": 2.2014909413218327e-10, "15": 1.9379866301805085e-11, "2": 0.11949296353521506, "3": 0.05171960980326946, "4": 0.017716031560500937, "5": 0.00499814828614042, "6": 0.0011957730164660846, "7": 0.0002479858146252714, "8": 4.53460532074804e-05, "9": 7.41077509308003e-06} |
| Raw goal margin distribution | {"-1": 0.18445704616259992, "-10": 4.915644062451468e-07, "-11": 6.110108638661574e-08, "-12": 6.9781564063254145e-09, "-13": 7.367387376294111e-10, "-14": 7.179481984436342e-11, "-15": 5.8340230620103006e-12, "-2": 0.10181802004661171, "-3": 0.04067979097242165, "-4": 0.012862668467906862, "-5": 0.0033497695083884883, "-6": 0.0007397682619733353, "-7": 0.00014161685404908564, "-8": 2.3903899520143902e-05, "-9": 3.6060691640887348e-06, "0": 0.26015049260152073, "1": 0.2003482255485063, "10": 1.0943817744916683e-06, "11": 1.4736562753871493e-07, "12": 1.823252456644227e-08, "13": 2.085347597385789e-09, "14": 2.2014909413218327e-10, "15": 1.9379866301805085e-11, "2": 0.11949296353521506, "3": 0.05171960980326946, "4": 0.017716031560500937, "5": 0.00499814828614042, "6": 0.0011957730164660846, "7": 0.0002479858146252714, "8": 4.53460532074804e-05, "9": 7.41077509308003e-06} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Toulouse", "away_goals": 0.0, "away_xg": 1.9, "date": "2026-11-01T00:00:00+00:00", "home": "Marseille", "home_goals": 2.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Troyes", "away_goals": 0.0, "away_xg": 0.39, "date": "2026-10-25T00:00:00+00:00", "home": "Toulouse", "home_goals": 0.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 3.0, "away_xg": 1.81, "date": "2026-10-16T00:00:00+00:00", "home": "Le Mans", "home_goals": 0.0, "home_xg": 0.95, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 2.0, "away_xg": 1.43, "date": "2026-10-10T00:00:00+00:00", "home": "Monaco", "home_goals": 2.0, "home_xg": 1.17, "source": "pipeline training history"}, {"away": "Le Havre", "away_goals": 2.0, "away_xg": 2.34, "date": "2026-09-19T00:00:00+00:00", "home": "Toulouse", "home_goals": 3.0, "home_xg": 1.95, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 2.0, "away_xg": 1.63, "date": "2026-09-12T00:00:00+00:00", "home": "Lorient", "home_goals": 2.0, "home_xg": 0.94, "source": "pipeline training history"}, {"away": "Lille", "away_goals": 1.0, "away_xg": 1.07, "date": "2026-09-03T00:00:00+00:00", "home": "Toulouse", "home_goals": 0.0, "home_xg": 3.41, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 2.0, "away_xg": 1.12, "date": "2026-08-29T00:00:00+00:00", "home": "Brest", "home_goals": 2.0, "home_xg": 2.73, "source": "pipeline training history"}, {"away": "Lyon", "away_goals": 2.0, "away_xg": 0.7, "date": "2026-08-22T00:00:00+00:00", "home": "Toulouse", "home_goals": 0.0, "home_xg": 2.76, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 0.0, "away_xg": null, "date": "2026-05-17T00:00:00+00:00", "home": "Nantes", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 34.4% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.1% |
| Raw p btts yes | 59.0% |
| P home draw | 65.6% |
| P draw away | 60.4% |
| P home away | 74.0% |
| Raw p home draw | 65.6% |
| Raw p draw away | 60.4% |
| Raw p home away | 74.0% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5524 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Count model | {"corners": {"alpha": 0.015413236227799179, "mu": 9.118241731788824, "version": "count-markets-nb2-v1"}} |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,453.8748 |
| Elo away rating | 1,507.0944 |
| Elo rating diff | 6.7804 |
| Elo home expectancy | 0.5098 |
| Research p home | 0.4020 |
| Research p draw | 0.2476 |
| Research p away | 0.3503 |
| Research p over 1 5 | 0.7843 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.5043577675119273, 1.3886483755347443], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:27:31.943510+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/fra.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-05T16:27:31.998847+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/fra.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:27:32.206426+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22Toulouse+FC%22+%22RC+Strasbourg+Alsace%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:27:32.314397+00:00", "reason": null, "status": "available", "url": "https://understat.com/league/Ligue_1/2026"}, {"observed_at_utc": "2026-11-05T16:27:32.419282+00:00", "reason": null, "status": "available", "url": "https://understat.com/league/Ligue_1/2025"}, {"observed_at_utc": "2026-11-05T16:27:13.451062+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:27:13.702984+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:27:32.518551+00:00", "reason": "HTTPError", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Toulouse+FC_vs_RC+Strasbourg+Alsace&d=2026-11-06"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 1.2636152888822214, "goals_for": 1.2209651152670602, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 1.1552120600883142, "results": "LDWDWDLDLD", "xg_against": 1.2106403766875036, "xg_for": 1.7616272267678712, "xg_matches": 9}, "venue": {"goals_against": 1.1612768438259973, "goals_for": 0.7942586323126342, "last_match": "2026-10-25T00:00:00+00:00", "matches": 4, "points_per_game": 1.0983798271058733, "results": "DWLL", "xg_against": 1.1251950322490534, "xg_for": 2.11144997355446, "xg_matches": 4}}}, "goal_rates": [1.5043577675119273, 1.3886483755347443], "h2h": [], "margin_distribution": {"-1": 0.1907127853884284, "-10": 4.915644062451467e-07, "-11": 6.110108638661573e-08, "-12": 6.978156406325414e-09, "-13": 7.367387376294111e-10, "-14": 7.17948198443634e-11, "-15": 5.8340230620103e-12, "-2": 0.1018180200466117, "-3": 0.04067979097242165, "-4": 0.01286266846790686, "-5": 0.003349769508388488, "-6": 0.0007397682619733351, "-7": 0.0001416168540490856, "-8": 2.3903899520143896e-05, "-9": 3.6060691640887344e-06, "0": 0.24763901414986378, "1": 0.20660396477433474, "10": 1.0943817744916683e-06, "11": 1.4736562753871493e-07, "12": 1.823252456644227e-08, "13": 2.085347597385789e-09, "14": 2.2014909413218327e-10, "15": 1.937986630180508e-11, "2": 0.11949296353521505, "3": 0.05171960980326945, "4": 0.017716031560500937, "5": 0.0049981482861404195, "6": 0.0011957730164660844, "7": 0.00024798581462527136, "8": 4.5346053207480396e-05, "9": 7.41077509308003e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:27:32.518974+00:00", "p_over_1_5": 0.7842908909799378, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
