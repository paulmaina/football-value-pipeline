# Pinnacle totals anchoring trial

Separate proportional intensity scaling to fresh Pinnacle O/U 2.5, fitted rho and production HDA preserved. Primary Under 3.5 log loss; other markets are guardrails. No bets, automatic promotion or backfill.

Status: COLLECT_MORE_DATA; paired fixtures: 3; gameweeks: 1

{
  "under_3_5": {
    "baseline": {
      "n": 3,
      "log_loss": 0.3682831033356357,
      "brier": 0.09996913462911304,
      "rps": null,
      "calibration": [
        {
          "low": 0.5,
          "high": 0.6,
          "n": 1,
          "mean_probability": 0.5698150907054242,
          "observed_rate": 1.0,
          "overconfidence": -0.43018490929457576,
          "observed_wilson95": [
            0.20654329147389294,
            1
          ]
        },
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 1,
          "mean_probability": 0.7253278523267723,
          "observed_rate": 1.0,
          "overconfidence": -0.2746721476732277,
          "observed_wilson95": [
            0.20654329147389294,
            1
          ]
        },
        {
          "low": 0.8,
          "high": 0.9,
          "n": 1,
          "mean_probability": 0.8014967028104235,
          "observed_rate": 1.0,
          "overconfidence": -0.1985032971895765,
          "observed_wilson95": [
            0.20654329147389294,
            1
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.8,
        "n": 1,
        "mean_probability": 0.8014967028104235,
        "observed_rate": 1.0
      }
    },
    "candidate": {
      "n": 3,
      "log_loss": 0.3221735257386445,
      "brier": 0.07605619351429467,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 3,
          "mean_probability": 0.724790646745903,
          "observed_rate": 1.0,
          "overconfidence": -0.275209353254097,
          "observed_wilson95": [
            0.43849391955098227,
            1
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.8,
        "n": 0,
        "mean_probability": null,
        "observed_rate": null
      }
    }
  },
  "over_1_5": {
    "baseline": {
      "n": 3,
      "log_loss": 0.2817914730595817,
      "brier": 0.06395084275418021,
      "rps": null,
      "calibration": [
        {
          "low": 0.6000000000000001,
          "high": 0.7000000000000001,
          "n": 1,
          "mean_probability": 0.6692560364388662,
          "observed_rate": 1.0,
          "overconfidence": -0.3307439635611338,
          "observed_wilson95": [
            0.20654329147389294,
            1
          ]
        },
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 1,
          "mean_probability": 0.7558148749067058,
          "observed_rate": 1.0,
          "overconfidence": -0.24418512509329415,
          "observed_wilson95": [
            0.20654329147389294,
            1
          ]
        },
        {
          "low": 0.8,
          "high": 0.9,
          "n": 1,
          "mean_probability": 0.8488888372303874,
          "observed_rate": 1.0,
          "overconfidence": -0.15111116276961256,
          "observed_wilson95": [
            0.20654329147389294,
            1
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.78,
        "n": 1,
        "mean_probability": 0.8488888372303874,
        "observed_rate": 1.0
      }
    },
    "candidate": {
      "n": 3,
      "log_loss": 0.29084182778749357,
      "brier": 0.0639515851128066,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 3,
          "mean_probability": 0.7478973866470046,
          "observed_rate": 1.0,
          "overconfidence": -0.25210261335299544,
          "observed_wilson95": [
            0.43849391955098227,
            1
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.78,
        "n": 0,
        "mean_probability": null,
        "observed_rate": null
      }
    }
  },
  "btts_yes": {
    "baseline": {
      "n": 3,
      "log_loss": 0.588623030944056,
      "brier": 0.19898896986036654,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 1,
          "mean_probability": 0.43526626872051316,
          "observed_rate": 0.0,
          "overconfidence": 0.43526626872051316,
          "observed_wilson95": [
            0,
            0.7934567085261071
          ]
        },
        {
          "low": 0.5,
          "high": 0.6,
          "n": 1,
          "mean_probability": 0.5317866831334589,
          "observed_rate": 0.0,
          "overconfidence": 0.5317866831334589,
          "observed_wilson95": [
            0,
            0.7934567085261071
          ]
        },
        {
          "low": 0.6000000000000001,
          "high": 0.7000000000000001,
          "n": 1,
          "mean_probability": 0.6468525682705085,
          "observed_rate": 1.0,
          "overconfidence": -0.3531474317294915,
          "observed_wilson95": [
            0.20654329147389294,
            1
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.7,
        "n": 0,
        "mean_probability": null,
        "observed_rate": null
      }
    },
    "candidate": {
      "n": 3,
      "log_loss": 0.7150355634266689,
      "brier": 0.260875691995438,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 1,
          "mean_probability": 0.49413662119864793,
          "observed_rate": 0.0,
          "overconfidence": 0.49413662119864793,
          "observed_wilson95": [
            0,
            0.7934567085261071
          ]
        },
        {
          "low": 0.5,
          "high": 0.6,
          "n": 2,
          "mean_probability": 0.5350603627398005,
          "observed_rate": 0.5,
          "overconfidence": 0.03506036273980051,
          "observed_wilson95": [
            0.09452865480086614,
            0.9054713451991339
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.7,
        "n": 0,
        "mean_probability": null,
        "observed_rate": null
      }
    }
  },
  "over_2_5": {
    "baseline": {
      "n": 3,
      "log_loss": 0.8765802911481261,
      "brier": 0.33954557532323676,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 2,
          "mean_probability": 0.44955401314410864,
          "observed_rate": 0.5,
          "overconfidence": -0.050445986855891356,
          "observed_wilson95": [
            0.09452865480086614,
            0.9054713451991339
          ]
        },
        {
          "low": 0.6000000000000001,
          "high": 0.7000000000000001,
          "n": 1,
          "mean_probability": 0.6434785595791882,
          "observed_rate": 0.0,
          "overconfidence": 0.6434785595791882,
          "observed_wilson95": [
            0,
            0.7934567085261071
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.7,
        "n": 0,
        "mean_probability": null,
        "observed_rate": null
      }
    },
    "candidate": {
      "n": 3,
      "log_loss": 0.7291230588355572,
      "brier": 0.2679643892799674,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 2,
          "mean_probability": 0.4812371402562873,
          "observed_rate": 0.5,
          "overconfidence": -0.018762859743712723,
          "observed_wilson95": [
            0.09452865480086614,
            0.9054713451991339
          ]
        },
        {
          "low": 0.5,
          "high": 0.6,
          "n": 1,
          "mean_probability": 0.5201334853882498,
          "observed_rate": 0.0,
          "overconfidence": 0.5201334853882498,
          "observed_wilson95": [
            0,
            0.7934567085261071
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.7,
        "n": 0,
        "mean_probability": null,
        "observed_rate": null
      }
    }
  }
}
