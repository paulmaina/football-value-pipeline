# Benchmark forward trial

Primary 1X2 log loss; week-block bootstrap, one preregistered candidate. Calibration and subgroup metrics are descriptive. Ready means enough evidence to review, including negative findings; it does not mean approval or profitability. Baseline is the actual production forecast. No closing odds, backfill, bets or automatic promotion.

Candidate: market-weight-085-v1; status: **COLLECT_MORE_DATA**; evidence: NO_CLEAR_PROMOTION_EVIDENCE.

Paired fixtures: 130/300; gameweeks: 3/6; verified coverage: 0.9629629629629629.

Comparison: {"baseline": {"n": 130, "log_loss": 0.9404792286975798, "brier": 0.5560308672599994, "rps": 0.19975296806427079, "calibration": [], "top_label_calibration": [{"band": 3, "n": 22, "mean_probability": 0.3813457774766484, "observed_rate": 0.36363636363636365, "gap": 0.017709413840284738}, {"band": 4, "n": 41, "mean_probability": 0.4483834288333955, "observed_rate": 0.5609756097560976, "gap": -0.11259218092270212}, {"band": 5, "n": 35, "mean_probability": 0.55742479726129, "observed_rate": 0.45714285714285713, "gap": 0.10028194011843289}, {"band": 6, "n": 20, "mean_probability": 0.6436357472284016, "observed_rate": 0.7, "gap": -0.0563642527715984}, {"band": 7, "n": 9, "mean_probability": 0.7369968984070511, "observed_rate": 1.0, "gap": -0.26300310159294893}, {"band": 8, "n": 3, "mean_probability": 0.8390969955462374, "observed_rate": 1.0, "gap": -0.1609030044537626}], "ece": 0.09609828007378461}, "candidate": {"n": 130, "log_loss": 0.9381132859929509, "brier": 0.5540228928460847, "rps": 0.19894968728790546, "calibration": [], "top_label_calibration": [{"band": 3, "n": 13, "mean_probability": 0.38303584741956226, "observed_rate": 0.46153846153846156, "gap": -0.0785026141188993}, {"band": 4, "n": 46, "mean_probability": 0.4381034312131996, "observed_rate": 0.5434782608695652, "gap": -0.10537482965636558}, {"band": 5, "n": 35, "mean_probability": 0.5518002787093034, "observed_rate": 0.4857142857142857, "gap": 0.06608599299501766}, {"band": 6, "n": 23, "mean_probability": 0.6489183355106145, "observed_rate": 0.7391304347826086, "gap": -0.09021209927199414}, {"band": 7, "n": 10, "mean_probability": 0.7465734243024984, "observed_rate": 0.9, "gap": -0.15342657569750162}, {"band": 8, "n": 3, "mean_probability": 0.8442905180142529, "observed_rate": 1.0, "gap": -0.15570948198574708}], "ece": 0.09428506452886344}, "log_loss_gain": 0.002365942704628976, "brier_gain": 0.0020079744139146483, "rps_gain": 0.0008032807763653227}

Week-block 95% log-loss gain interval: [-0.0036984613456176735, 0.011456412407980832].

Excluded forecasts by reason: incoherent_reference_prices: 14, invalid_probability_simplex: 14, league_outside_frozen_trial: 101, missing_stale_or_future_reference: 14, no_live_blended_reference: 14, production_weight_outside_frozen_trial: 14, unreliable_team_identity: 16

Production changes require your review and approval.
