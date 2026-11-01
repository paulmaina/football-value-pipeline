# Benchmark forward trial

Primary 1X2 log loss; week-block bootstrap, one preregistered candidate. Calibration and subgroup metrics are descriptive. Ready means enough evidence to review, including negative findings; it does not mean approval or profitability. Baseline is the actual production forecast. No closing odds, backfill, bets or automatic promotion.

Candidate: market-weight-085-v1; status: **COLLECT_MORE_DATA**; evidence: NO_CLEAR_PROMOTION_EVIDENCE.

Paired fixtures: 117/300; gameweeks: 3/6; verified coverage: 0.9831932773109243.

Comparison: {"baseline": {"n": 117, "log_loss": 0.9558243209060195, "brier": 0.5670554253455509, "rps": 0.20219182316955195, "calibration": [], "top_label_calibration": [{"band": 3, "n": 18, "mean_probability": 0.3814832053722305, "observed_rate": 0.2777777777777778, "gap": 0.10370542759445273}, {"band": 4, "n": 37, "mean_probability": 0.4513126284743226, "observed_rate": 0.5675675675675675, "gap": -0.11625493909324497}, {"band": 5, "n": 32, "mean_probability": 0.5576174490183398, "observed_rate": 0.40625, "gap": 0.15136744901833976}, {"band": 6, "n": 19, "mean_probability": 0.6442562519970385, "observed_rate": 0.6842105263157895, "gap": -0.03995427431875098}, {"band": 7, "n": 9, "mean_probability": 0.7369968984070511, "observed_rate": 1.0, "gap": -0.26300310159294893}, {"band": 8, "n": 2, "mean_probability": 0.847603936327515, "observed_rate": 1.0, "gap": -0.15239606367248504}], "ece": 0.12344307748269115}, "candidate": {"n": 117, "log_loss": 0.9526360147037706, "brier": 0.5645354557698917, "rps": 0.20115857752466904, "calibration": [], "top_label_calibration": [{"band": 3, "n": 10, "mean_probability": 0.3833906512444034, "observed_rate": 0.5, "gap": -0.11660934875559659}, {"band": 4, "n": 41, "mean_probability": 0.4404224305134535, "observed_rate": 0.5121951219512195, "gap": -0.07177269143776605}, {"band": 5, "n": 33, "mean_probability": 0.553559019612832, "observed_rate": 0.45454545454545453, "gap": 0.09901356506737752}, {"band": 6, "n": 21, "mean_probability": 0.6505596082158941, "observed_rate": 0.7142857142857143, "gap": -0.06372610606982021}, {"band": 7, "n": 10, "mean_probability": 0.7465734243024984, "observed_rate": 0.9, "gap": -0.15342657569750162}, {"band": 8, "n": 2, "mean_probability": 0.855487007266422, "observed_rate": 1.0, "gap": -0.14451299273357798}], "ece": 0.09006633721056606}, "log_loss_gain": 0.0031883062022489694, "brier_gain": 0.0025199695756591423, "rps_gain": 0.001033245644882913}

Week-block 95% log-loss gain interval: [-0.0032019105865232294, 0.011456412407980832].

Excluded forecasts by reason: incoherent_reference_prices: 14, invalid_probability_simplex: 14, league_outside_frozen_trial: 101, missing_stale_or_future_reference: 14, no_live_blended_reference: 14, production_weight_outside_frozen_trial: 14, unreliable_team_identity: 16

Production changes require your review and approval.
