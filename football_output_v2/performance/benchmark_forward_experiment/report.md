# Benchmark forward trial

Primary 1X2 log loss; week-block bootstrap, one preregistered candidate. Calibration and subgroup metrics are descriptive. Ready means enough evidence to review, including negative findings; it does not mean approval or profitability. Baseline is the actual production forecast. No closing odds, backfill, bets or automatic promotion.

Candidate: market-weight-085-v1; status: **COLLECT_MORE_DATA**; evidence: NO_CLEAR_PROMOTION_EVIDENCE.

Paired fixtures: 82/300; gameweeks: 2/6; verified coverage: 0.9761904761904762.

Comparison: {"baseline": {"n": 82, "log_loss": 0.9606699991996932, "brier": 0.5715096787325958, "rps": 0.1996983542439092, "calibration": [], "top_label_calibration": [{"band": 3, "n": 13, "mean_probability": 0.3830174829756162, "observed_rate": 0.3076923076923077, "gap": 0.07532517528330851}, {"band": 4, "n": 25, "mean_probability": 0.44664487330952424, "observed_rate": 0.6, "gap": -0.15335512669047574}, {"band": 5, "n": 21, "mean_probability": 0.551809322034083, "observed_rate": 0.2857142857142857, "gap": 0.26609503631979725}, {"band": 6, "n": 17, "mean_probability": 0.640083938526739, "observed_rate": 0.7647058823529411, "gap": -0.12462194382620218}, {"band": 7, "n": 5, "mean_probability": 0.7337553562357539, "observed_rate": 1.0, "gap": -0.26624464376424606}, {"band": 8, "n": 1, "mean_probability": 0.838375817695898, "observed_rate": 1.0, "gap": -0.16162418230410203}], "ece": 0.17088441042477337}, "candidate": {"n": 82, "log_loss": 0.9547541614412611, "brier": 0.5670301373104879, "rps": 0.19764032173237928, "calibration": [], "top_label_calibration": [{"band": 3, "n": 6, "mean_probability": 0.38017852557107795, "observed_rate": 0.5, "gap": -0.11982147442892205}, {"band": 4, "n": 30, "mean_probability": 0.4363789453137523, "observed_rate": 0.5666666666666667, "gap": -0.13028772135291433}, {"band": 5, "n": 22, "mean_probability": 0.5513694202899821, "observed_rate": 0.36363636363636365, "gap": 0.1877330566536185}, {"band": 6, "n": 18, "mean_probability": 0.6526845084750585, "observed_rate": 0.7222222222222222, "gap": -0.06953771374716367}, {"band": 7, "n": 5, "mean_probability": 0.7515007145868312, "observed_rate": 1.0, "gap": -0.2484992854131688}, {"band": 8, "n": 1, "mean_probability": 0.8175572083916254, "observed_rate": 1.0, "gap": -0.18244279160837462}], "ece": 0.13944275365443579}, "log_loss_gain": 0.005915837758432074, "brier_gain": 0.0044795414221079355, "rps_gain": 0.002058032511529917}

Week-block 95% log-loss gain interval: [0.0015797358587853133, 0.011456412407980832].

Excluded forecasts by reason: league_outside_frozen_trial: 55, unreliable_team_identity: 16

Production changes require your review and approval.
