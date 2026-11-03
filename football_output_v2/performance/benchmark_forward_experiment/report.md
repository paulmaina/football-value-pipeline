# Benchmark forward trial

Primary 1X2 log loss; week-block bootstrap, one preregistered candidate. Calibration and subgroup metrics are descriptive. Ready means enough evidence to review, including negative findings; it does not mean approval or profitability. Baseline is the actual production forecast. No closing odds, backfill, bets or automatic promotion.

Candidate: market-weight-085-v1; status: **COLLECT_MORE_DATA**; evidence: NO_CLEAR_PROMOTION_EVIDENCE.

Paired fixtures: 135/300; gameweeks: 4/6; verified coverage: 0.9574468085106383.

Comparison: {"baseline": {"n": 135, "log_loss": 0.9488721585150189, "brier": 0.5615146581400334, "rps": 0.20413193637079202, "calibration": [], "top_label_calibration": [{"band": 3, "n": 23, "mean_probability": 0.3809946463619199, "observed_rate": 0.34782608695652173, "gap": 0.033168559405398146}, {"band": 4, "n": 44, "mean_probability": 0.44765544623397824, "observed_rate": 0.5681818181818182, "gap": -0.12052637194784}, {"band": 5, "n": 35, "mean_probability": 0.55742479726129, "observed_rate": 0.45714285714285713, "gap": 0.10028194011843289}, {"band": 6, "n": 21, "mean_probability": 0.643616183703038, "observed_rate": 0.6666666666666666, "gap": -0.02305048296362866}, {"band": 7, "n": 9, "mean_probability": 0.7369968984070511, "observed_rate": 1.0, "gap": -0.26300310159294893}, {"band": 8, "n": 3, "mean_probability": 0.8390969955462374, "observed_rate": 1.0, "gap": -0.1609030044537626}], "ece": 0.09562742374895035}, "candidate": {"n": 135, "log_loss": 0.9465067428273554, "brier": 0.5596547830507299, "rps": 0.20337856096511103, "calibration": [], "top_label_calibration": [{"band": 3, "n": 14, "mean_probability": 0.38285162785989846, "observed_rate": 0.42857142857142855, "gap": -0.04571980071153009}, {"band": 4, "n": 49, "mean_probability": 0.4373863771337542, "observed_rate": 0.5510204081632653, "gap": -0.11363403102951103}, {"band": 5, "n": 35, "mean_probability": 0.5518002787093034, "observed_rate": 0.4857142857142857, "gap": 0.06608599299501766}, {"band": 6, "n": 24, "mean_probability": 0.6487841709240266, "observed_rate": 0.7083333333333334, "gap": -0.059549162409306744}, {"band": 7, "n": 10, "mean_probability": 0.7465734243024984, "observed_rate": 0.9, "gap": -0.15342657569750162}, {"band": 8, "n": 3, "mean_probability": 0.8442905180142529, "observed_rate": 1.0, "gap": -0.15570948198574708}], "ece": 0.08853132285917555}, "log_loss_gain": 0.0023654156876635746, "brier_gain": 0.0018598750893035199, "rps_gain": 0.0007533754056809894}

Week-block 95% log-loss gain interval: [-0.0031276901576764104, 0.010346083241953867].

Excluded forecasts by reason: incoherent_reference_prices: 14, invalid_probability_simplex: 14, league_outside_frozen_trial: 101, missing_stale_or_future_reference: 14, no_live_blended_reference: 14, production_weight_outside_frozen_trial: 14, unreliable_team_identity: 16

Production changes require your review and approval.
