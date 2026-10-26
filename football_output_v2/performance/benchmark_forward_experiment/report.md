# Benchmark forward trial

Primary 1X2 log loss; week-block bootstrap, one preregistered candidate. Calibration and subgroup metrics are descriptive. Ready means enough evidence to review, including negative findings; it does not mean approval or profitability. Baseline is the actual production forecast. No closing odds, backfill, bets or automatic promotion.

Candidate: market-weight-085-v1; status: **COLLECT_MORE_DATA**; evidence: NO_CLEAR_PROMOTION_EVIDENCE.

Paired fixtures: 83/300; gameweeks: 3/6; verified coverage: 0.9764705882352941.

Comparison: {"baseline": {"n": 83, "log_loss": 0.9575599675224261, "brier": 0.5692322536541135, "rps": 0.19916641924060863, "calibration": [], "top_label_calibration": [{"band": 3, "n": 13, "mean_probability": 0.3830174829756162, "observed_rate": 0.3076923076923077, "gap": 0.07532517528330851}, {"band": 4, "n": 26, "mean_probability": 0.4485172581962312, "observed_rate": 0.6153846153846154, "gap": -0.1668673571883842}, {"band": 5, "n": 21, "mean_probability": 0.551809322034083, "observed_rate": 0.2857142857142857, "gap": 0.26609503631979725}, {"band": 6, "n": 17, "mean_probability": 0.640083938526739, "observed_rate": 0.7647058823529411, "gap": -0.12462194382620218}, {"band": 7, "n": 5, "mean_probability": 0.7337553562357539, "observed_rate": 1.0, "gap": -0.26624464376424606}, {"band": 8, "n": 1, "mean_probability": 0.838375817695898, "observed_rate": 1.0, "gap": -0.16162418230410203}], "ece": 0.17490596113816279}, "candidate": {"n": 83, "log_loss": 0.9515589723529366, "brier": 0.5646919368732177, "rps": 0.19707578155457658, "calibration": [], "top_label_calibration": [{"band": 3, "n": 6, "mean_probability": 0.38017852557107795, "observed_rate": 0.5, "gap": -0.11982147442892205}, {"band": 4, "n": 30, "mean_probability": 0.4363789453137523, "observed_rate": 0.5666666666666667, "gap": -0.13028772135291433}, {"band": 5, "n": 23, "mean_probability": 0.5492142319856368, "observed_rate": 0.391304347826087, "gap": 0.15790988415954982}, {"band": 6, "n": 18, "mean_probability": 0.6526845084750585, "observed_rate": 0.7222222222222222, "gap": -0.06953771374716367}, {"band": 7, "n": 5, "mean_probability": 0.7515007145868312, "observed_rate": 1.0, "gap": -0.2484992854131688}, {"band": 8, "n": 1, "mean_probability": 0.8175572083916254, "observed_rate": 1.0, "gap": -0.18244279160837462}], "ece": 0.1317603119151057}, "log_loss_gain": 0.006000995169489487, "brier_gain": 0.004540316780895726, "rps_gain": 0.002090637686032043}

Week-block 95% log-loss gain interval: [0.0015797358587853133, 0.01298390287619755].

Excluded forecasts by reason: league_outside_frozen_trial: 55, unreliable_team_identity: 16

Production changes require your review and approval.
