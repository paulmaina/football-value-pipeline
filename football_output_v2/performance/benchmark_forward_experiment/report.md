# Benchmark forward trial

Primary 1X2 log loss; week-block bootstrap, one preregistered candidate. Calibration and subgroup metrics are descriptive. Ready means enough evidence to review, including negative findings; it does not mean approval or profitability. Baseline is the actual production forecast. No closing odds, backfill, bets or automatic promotion.

Candidate: market-weight-085-v1; status: **COLLECT_MORE_DATA**; evidence: NO_CLEAR_PROMOTION_EVIDENCE.

Paired fixtures: 128/300; gameweeks: 3/6; verified coverage: 0.9696969696969697.

Comparison: {"baseline": {"n": 128, "log_loss": 0.9429642355992603, "brier": 0.5578465349384027, "rps": 0.19998604424954874, "calibration": [], "top_label_calibration": [{"band": 3, "n": 21, "mean_probability": 0.380897617475913, "observed_rate": 0.3333333333333333, "gap": 0.04756428414257968}, {"band": 4, "n": 41, "mean_probability": 0.4483834288333955, "observed_rate": 0.5609756097560976, "gap": -0.11259218092270212}, {"band": 5, "n": 34, "mean_probability": 0.5580484326923649, "observed_rate": 0.4411764705882353, "gap": 0.11687196210412965}, {"band": 6, "n": 20, "mean_probability": 0.6436357472284016, "observed_rate": 0.7, "gap": -0.0563642527715984}, {"band": 7, "n": 9, "mean_probability": 0.7369968984070511, "observed_rate": 1.0, "gap": -0.26300310159294893}, {"band": 8, "n": 3, "mean_probability": 0.8390969955462374, "observed_rate": 1.0, "gap": -0.1609030044537626}], "ece": 0.10598279749605598}, "candidate": {"n": 128, "log_loss": 0.9406632839735342, "brier": 0.555872043453775, "rps": 0.19919121476199647, "calibration": [], "top_label_calibration": [{"band": 3, "n": 13, "mean_probability": 0.38303584741956226, "observed_rate": 0.46153846153846156, "gap": -0.0785026141188993}, {"band": 4, "n": 45, "mean_probability": 0.43868485890624237, "observed_rate": 0.5333333333333333, "gap": -0.09464847442709096}, {"band": 5, "n": 34, "mean_probability": 0.5528729259923123, "observed_rate": 0.47058823529411764, "gap": 0.08228469069819466}, {"band": 6, "n": 23, "mean_probability": 0.6489183355106145, "observed_rate": 0.7391304347826086, "gap": -0.09021209927199414}, {"band": 7, "n": 10, "mean_probability": 0.7465734243024984, "observed_rate": 0.9, "gap": -0.15342657569750162}, {"band": 8, "n": 3, "mean_probability": 0.8442905180142529, "observed_rate": 1.0, "gap": -0.15570948198574708}], "ece": 0.09495052580227753}, "log_loss_gain": 0.0023009516257261886, "brier_gain": 0.001974491484627694, "rps_gain": 0.0007948294875522732}

Week-block 95% log-loss gain interval: [-0.004142975828227939, 0.011456412407980832].

Excluded forecasts by reason: incoherent_reference_prices: 14, invalid_probability_simplex: 14, league_outside_frozen_trial: 101, missing_stale_or_future_reference: 14, no_live_blended_reference: 14, production_weight_outside_frozen_trial: 14, unreliable_team_identity: 16

Production changes require your review and approval.
