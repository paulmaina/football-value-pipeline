# Benchmark forward trial

Primary 1X2 log loss; week-block bootstrap, one preregistered candidate. Calibration and subgroup metrics are descriptive. Ready means enough evidence to review, including negative findings; it does not mean approval or profitability. Baseline is the actual production forecast. No closing odds, backfill, bets or automatic promotion.

Candidate: market-weight-085-v1; status: **COLLECT_MORE_DATA**; evidence: NO_CLEAR_PROMOTION_EVIDENCE.

Paired fixtures: 113/300; gameweeks: 3/6; verified coverage: 0.9826086956521739.

Comparison: {"baseline": {"n": 113, "log_loss": 0.9559326383213608, "brier": 0.5666215402794882, "rps": 0.20208327631315257, "calibration": [], "top_label_calibration": [{"band": 3, "n": 17, "mean_probability": 0.38202213979555943, "observed_rate": 0.29411764705882354, "gap": 0.0879044927367359}, {"band": 4, "n": 35, "mean_probability": 0.4491931702969977, "observed_rate": 0.6, "gap": -0.1508068297030023}, {"band": 5, "n": 32, "mean_probability": 0.5576174490183398, "observed_rate": 0.40625, "gap": 0.15136744901833976}, {"band": 6, "n": 19, "mean_probability": 0.6442562519970385, "observed_rate": 0.6842105263157895, "gap": -0.03995427431875098}, {"band": 7, "n": 9, "mean_probability": 0.7369968984070511, "observed_rate": 1.0, "gap": -0.26300310159294893}, {"band": 8, "n": 1, "mean_probability": 0.838375817695898, "observed_rate": 1.0, "gap": -0.16162418230410203}], "ece": 0.13189519551693252}, "candidate": {"n": 113, "log_loss": 0.9532694399639351, "brier": 0.5644305439161522, "rps": 0.20129142568104116, "calibration": [], "top_label_calibration": [{"band": 3, "n": 9, "mean_probability": 0.3818037062468397, "observed_rate": 0.4444444444444444, "gap": -0.06264073819760474}, {"band": 4, "n": 39, "mean_probability": 0.4378491439849408, "observed_rate": 0.5384615384615384, "gap": -0.10061239447659764}, {"band": 5, "n": 33, "mean_probability": 0.553559019612832, "observed_rate": 0.45454545454545453, "gap": 0.09901356506737752}, {"band": 6, "n": 21, "mean_probability": 0.6505596082158941, "observed_rate": 0.7142857142857143, "gap": -0.06372610606982021}, {"band": 7, "n": 10, "mean_probability": 0.7465734243024984, "observed_rate": 0.9, "gap": -0.15342657569750162}, {"band": 8, "n": 1, "mean_probability": 0.8175572083916254, "observed_rate": 1.0, "gap": -0.18244279160837462}], "ece": 0.09566419868706925}, "log_loss_gain": 0.002663198357425678, "brier_gain": 0.002190996363335973, "rps_gain": 0.0007918506321114016}

Week-block 95% log-loss gain interval: [-0.005940557477494887, 0.011456412407980832].

Excluded forecasts by reason: league_outside_frozen_trial: 82, unreliable_team_identity: 16

Production changes require your review and approval.
