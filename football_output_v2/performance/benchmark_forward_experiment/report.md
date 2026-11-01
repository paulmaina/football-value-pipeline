# Benchmark forward trial

Primary 1X2 log loss; week-block bootstrap, one preregistered candidate. Calibration and subgroup metrics are descriptive. Ready means enough evidence to review, including negative findings; it does not mean approval or profitability. Baseline is the actual production forecast. No closing odds, backfill, bets or automatic promotion.

Candidate: market-weight-085-v1; status: **COLLECT_MORE_DATA**; evidence: NO_CLEAR_PROMOTION_EVIDENCE.

Paired fixtures: 118/300; gameweeks: 3/6; verified coverage: 0.9833333333333333.

Comparison: {"baseline": {"n": 118, "log_loss": 0.95704910103658, "brier": 0.5679141654392313, "rps": 0.20288510531666062, "calibration": [], "top_label_calibration": [{"band": 3, "n": 19, "mean_probability": 0.37984742512483366, "observed_rate": 0.2631578947368421, "gap": 0.11668953038799157}, {"band": 4, "n": 37, "mean_probability": 0.4513126284743226, "observed_rate": 0.5675675675675675, "gap": -0.11625493909324497}, {"band": 5, "n": 32, "mean_probability": 0.5576174490183398, "observed_rate": 0.40625, "gap": 0.15136744901833976}, {"band": 6, "n": 19, "mean_probability": 0.6442562519970385, "observed_rate": 0.6842105263157895, "gap": -0.03995427431875098}, {"band": 7, "n": 9, "mean_probability": 0.7369968984070511, "observed_rate": 1.0, "gap": -0.26300310159294893}, {"band": 8, "n": 2, "mean_probability": 0.847603936327515, "observed_rate": 1.0, "gap": -0.15239606367248504}], "ece": 0.12536646988259792}, "candidate": {"n": 118, "log_loss": 0.954463716129884, "brier": 0.5657993612529022, "rps": 0.2020484989319153, "calibration": [], "top_label_calibration": [{"band": 3, "n": 11, "mean_probability": 0.3822433785080067, "observed_rate": 0.45454545454545453, "gap": -0.07230207603744782}, {"band": 4, "n": 41, "mean_probability": 0.4404224305134535, "observed_rate": 0.5121951219512195, "gap": -0.07177269143776605}, {"band": 5, "n": 33, "mean_probability": 0.553559019612832, "observed_rate": 0.45454545454545453, "gap": 0.09901356506737752}, {"band": 6, "n": 21, "mean_probability": 0.6505596082158941, "observed_rate": 0.7142857142857143, "gap": -0.06372610606982021}, {"band": 7, "n": 10, "mean_probability": 0.7465734243024984, "observed_rate": 0.9, "gap": -0.15342657569750162}, {"band": 8, "n": 2, "mean_probability": 0.855487007266422, "observed_rate": 1.0, "gap": -0.14451299273357798}], "ece": 0.08616093900417109}, "log_loss_gain": 0.00258538490669602, "brier_gain": 0.0021148041863291445, "rps_gain": 0.0008366063847453364}

Week-block 95% log-loss gain interval: [-0.005000646588924994, 0.011456412407980832].

Excluded forecasts by reason: incoherent_reference_prices: 14, invalid_probability_simplex: 14, league_outside_frozen_trial: 101, missing_stale_or_future_reference: 14, no_live_blended_reference: 14, production_weight_outside_frozen_trial: 14, unreliable_team_identity: 16

Production changes require your review and approval.
