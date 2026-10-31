# Benchmark forward trial

Primary 1X2 log loss; week-block bootstrap, one preregistered candidate. Calibration and subgroup metrics are descriptive. Ready means enough evidence to review, including negative findings; it does not mean approval or profitability. Baseline is the actual production forecast. No closing odds, backfill, bets or automatic promotion.

Candidate: market-weight-085-v1; status: **COLLECT_MORE_DATA**; evidence: NO_CLEAR_PROMOTION_EVIDENCE.

Paired fixtures: 96/300; gameweeks: 3/6; verified coverage: 0.9795918367346939.

Comparison: {"baseline": {"n": 96, "log_loss": 0.9593008298015654, "brier": 0.5687573239686675, "rps": 0.20215046108218818, "calibration": [], "top_label_calibration": [{"band": 3, "n": 16, "mean_probability": 0.38215166345459145, "observed_rate": 0.3125, "gap": 0.06965166345459145}, {"band": 4, "n": 28, "mean_probability": 0.44777472775591465, "observed_rate": 0.6071428571428571, "gap": -0.15936812938694245}, {"band": 5, "n": 25, "mean_probability": 0.5536395205234126, "observed_rate": 0.32, "gap": 0.23363952052341258}, {"band": 6, "n": 18, "mean_probability": 0.6419389355964141, "observed_rate": 0.7222222222222222, "gap": -0.08028328662580808}, {"band": 7, "n": 8, "mean_probability": 0.7360208695265731, "observed_rate": 1.0, "gap": -0.2639791304734269}, {"band": 8, "n": 1, "mean_probability": 0.838375817695898, "observed_rate": 1.0, "gap": -0.16162418230410203}], "ece": 0.15766956913072114}, "candidate": {"n": 96, "log_loss": 0.957643778403988, "brier": 0.5672182888941436, "rps": 0.20169112191202865, "calibration": [], "top_label_calibration": [{"band": 3, "n": 8, "mean_probability": 0.3803394968014841, "observed_rate": 0.5, "gap": -0.1196605031985159}, {"band": 4, "n": 33, "mean_probability": 0.436654085568529, "observed_rate": 0.5454545454545454, "gap": -0.10880045988601639}, {"band": 5, "n": 27, "mean_probability": 0.5530873081222422, "observed_rate": 0.4074074074074074, "gap": 0.14567990071483478}, {"band": 6, "n": 19, "mean_probability": 0.6544723501941384, "observed_rate": 0.6842105263157895, "gap": -0.029738176121651083}, {"band": 7, "n": 8, "mean_probability": 0.7524572537546402, "observed_rate": 1.0, "gap": -0.24754274624535977}, {"band": 8, "n": 1, "mean_probability": 0.8175572083916254, "observed_rate": 1.0, "gap": -0.18244279160837462}], "ece": 0.11675902738551906}, "log_loss_gain": 0.001657051397577436, "brier_gain": 0.001539035074523909, "rps_gain": 0.0004593391701595284}

Week-block 95% log-loss gain interval: [-0.023287268715999874, 0.011456412407980832].

Excluded forecasts by reason: league_outside_frozen_trial: 79, unreliable_team_identity: 16

Production changes require your review and approval.
