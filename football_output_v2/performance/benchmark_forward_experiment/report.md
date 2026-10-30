# Benchmark forward trial

Primary 1X2 log loss; week-block bootstrap, one preregistered candidate. Calibration and subgroup metrics are descriptive. Ready means enough evidence to review, including negative findings; it does not mean approval or profitability. Baseline is the actual production forecast. No closing odds, backfill, bets or automatic promotion.

Candidate: market-weight-085-v1; status: **COLLECT_MORE_DATA**; evidence: NO_CLEAR_PROMOTION_EVIDENCE.

Paired fixtures: 93/300; gameweeks: 3/6; verified coverage: 0.9789473684210527.

Comparison: {"baseline": {"n": 93, "log_loss": 0.9473831506826315, "brier": 0.5607066037827105, "rps": 0.19640769077592393, "calibration": [], "top_label_calibration": [{"band": 3, "n": 15, "mean_probability": 0.38241429564617574, "observed_rate": 0.26666666666666666, "gap": 0.11574762897950908}, {"band": 4, "n": 27, "mean_probability": 0.4493450920493354, "observed_rate": 0.6296296296296297, "gap": -0.18028453758029422}, {"band": 5, "n": 25, "mean_probability": 0.5536395205234126, "observed_rate": 0.32, "gap": 0.23363952052341258}, {"band": 6, "n": 17, "mean_probability": 0.640083938526739, "observed_rate": 0.7647058823529411, "gap": -0.12462194382620218}, {"band": 7, "n": 8, "mean_probability": 0.7360208695265731, "observed_rate": 1.0, "gap": -0.2639791304734269}, {"band": 8, "n": 1, "mean_probability": 0.838375817695898, "observed_rate": 1.0, "gap": -0.16162418230410203}], "ece": 0.1810420992858371}, "candidate": {"n": 93, "log_loss": 0.9438986217157317, "brier": 0.5579463018766297, "rps": 0.1953095376942926, "calibration": [], "top_label_calibration": [{"band": 3, "n": 7, "mean_probability": 0.38112105637731303, "observed_rate": 0.42857142857142855, "gap": -0.04745037219411552}, {"band": 4, "n": 32, "mean_probability": 0.436576781455349, "observed_rate": 0.5625, "gap": -0.125923218544651}, {"band": 5, "n": 27, "mean_probability": 0.5530873081222422, "observed_rate": 0.4074074074074074, "gap": 0.14567990071483478}, {"band": 6, "n": 18, "mean_probability": 0.6526845084750585, "observed_rate": 0.7222222222222222, "gap": -0.06953771374716367}, {"band": 7, "n": 8, "mean_probability": 0.7524572537546402, "observed_rate": 1.0, "gap": -0.24754274624535977}, {"band": 8, "n": 1, "mean_probability": 0.8175572083916254, "observed_rate": 1.0, "gap": -0.18244279160837462}], "ece": 0.1259087798613804}, "log_loss_gain": 0.003484528966899769, "brier_gain": 0.0027603019060807865, "rps_gain": 0.0010981530816313312}

Week-block 95% log-loss gain interval: [-0.014639772933614396, 0.011456412407980832].

Excluded forecasts by reason: league_outside_frozen_trial: 79, unreliable_team_identity: 16

Production changes require your review and approval.
