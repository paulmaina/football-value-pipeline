# Benchmark forward trial

Primary 1X2 log loss; week-block bootstrap, one preregistered candidate. Calibration and subgroup metrics are descriptive. Ready means enough evidence to review, including negative findings; it does not mean approval or profitability. Baseline is the actual production forecast. No closing odds, backfill, bets or automatic promotion.

Candidate: market-weight-085-v1; status: **COLLECT_MORE_DATA**; evidence: NO_CLEAR_PROMOTION_EVIDENCE.

Paired fixtures: 64/300; gameweeks: 2/6; verified coverage: 0.9696969696969697.

Comparison: {"baseline": {"n": 64, "log_loss": 0.9404887889019857, "brier": 0.5559130214259145, "rps": 0.20289962923923124, "calibration": [], "top_label_calibration": [{"band": 3, "n": 11, "mean_probability": 0.38214718050882207, "observed_rate": 0.2727272727272727, "gap": 0.10941990778154936}, {"band": 4, "n": 18, "mean_probability": 0.4433257680036138, "observed_rate": 0.7222222222222222, "gap": -0.2788964542186084}, {"band": 5, "n": 16, "mean_probability": 0.5435039146155854, "observed_rate": 0.25, "gap": 0.29350391461558545}, {"band": 6, "n": 13, "mean_probability": 0.6412418456612239, "observed_rate": 0.7692307692307693, "gap": -0.1279889235695454}, {"band": 7, "n": 5, "mean_probability": 0.7337553562357539, "observed_rate": 1.0, "gap": -0.26624464376424606}, {"band": 8, "n": 1, "mean_probability": 0.838375817695898, "observed_rate": 1.0, "gap": -0.16162418230410203}], "ece": 0.219945643795481}, "candidate": {"n": 64, "log_loss": 0.935495243635355, "brier": 0.5515735635207694, "rps": 0.20081002011852067, "calibration": [], "top_label_calibration": [{"band": 3, "n": 5, "mean_probability": 0.3805863648644775, "observed_rate": 0.6, "gap": -0.21941363513552248}, {"band": 4, "n": 23, "mean_probability": 0.43189559880147477, "observed_rate": 0.6086956521739131, "gap": -0.17680005337243831}, {"band": 5, "n": 18, "mean_probability": 0.5501110070252646, "observed_rate": 0.3888888888888889, "gap": 0.1612221181363757}, {"band": 6, "n": 12, "mean_probability": 0.6608821023800225, "observed_rate": 0.75, "gap": -0.08911789761997746}, {"band": 7, "n": 5, "mean_probability": 0.7515007145868312, "observed_rate": 1.0, "gap": -0.2484992854131688}, {"band": 8, "n": 1, "mean_probability": 0.8175572083916254, "observed_rate": 1.0, "gap": -0.18244279160837462}], "ece": 0.16499721124706884}, "log_loss_gain": 0.004993545266630761, "brier_gain": 0.0043394579051451165, "rps_gain": 0.0020896091207105727}

Week-block 95% log-loss gain interval: [-0.0033158553436766153, 0.011456412407980832].

Excluded forecasts by reason: league_outside_frozen_trial: 55, unreliable_team_identity: 16

Production changes require your review and approval.
