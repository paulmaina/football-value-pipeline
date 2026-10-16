# Benchmark forward trial

Primary 1X2 log loss; week-block bootstrap, one preregistered candidate. Calibration and subgroup metrics are descriptive. Ready means enough evidence to review, including negative findings; it does not mean approval or profitability. Baseline is the actual production forecast. No closing odds, backfill, bets or automatic promotion.

Candidate: market-weight-085-v1; status: **COLLECT_MORE_DATA**; evidence: NO_CLEAR_PROMOTION_EVIDENCE.

Paired fixtures: 3/300; gameweeks: 1/6; verified coverage: 0.75.

Comparison: {"baseline": {"n": 3, "log_loss": 1.0993958955036407, "brier": 0.6720253086290532, "rps": 0.218666812586544, "calibration": [], "top_label_calibration": [{"band": 3, "n": 1, "mean_probability": 0.38054655056237513, "observed_rate": 0.0, "gap": 0.38054655056237513}, {"band": 4, "n": 1, "mean_probability": 0.4198361364008173, "observed_rate": 1.0, "gap": -0.5801638635991827}, {"band": 5, "n": 1, "mean_probability": 0.5040173094508038, "observed_rate": 0.0, "gap": 0.5040173094508038}], "ece": 0.4882425745374539}, "candidate": {"n": 3, "log_loss": 1.059998362838539, "brier": 0.6435837899259768, "rps": 0.20697751570287937, "calibration": [], "top_label_calibration": [{"band": 3, "n": 1, "mean_probability": 0.39608154153176556, "observed_rate": 1.0, "gap": -0.6039184584682344}, {"band": 4, "n": 2, "mean_probability": 0.441613295923464, "observed_rate": 0.5, "gap": -0.05838670407653601}], "ece": 0.24023062220710215}, "log_loss_gain": 0.03939753266510171, "brier_gain": 0.02844151870307643, "rps_gain": 0.01168929688366463}

Week-block 95% log-loss gain interval: None.

Production changes require your review and approval.
