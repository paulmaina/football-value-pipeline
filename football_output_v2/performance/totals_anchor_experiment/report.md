# Pinnacle totals anchoring trial

Separate proportional intensity scaling to fresh Pinnacle O/U 2.5, fitted rho and production HDA preserved. Primary Under 3.5 log loss; other markets are guardrails. No bets, automatic promotion or backfill.

Status: COLLECT_MORE_DATA; paired fixtures: 2; gameweeks: 1

{
  "under_3_5": {
    "baseline": {
      "n": 2,
      "log_loss": 0.391858896884581,
      "brier": 0.11223130758995786,
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
      "n": 2,
      "log_loss": 0.3069162758955836,
      "brier": 0.06991930444415273,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 2,
          "mean_probability": 0.7357877632225872,
          "observed_rate": 1.0,
          "overconfidence": -0.2642122367774128,
          "observed_wilson95": [
            0.34237195288961925,
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
      "n": 2,
      "log_loss": 0.28270780596373263,
      "brier": 0.06611307647285647,
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
      "n": 2,
      "log_loss": 0.30810686236975965,
      "brier": 0.07036692211542356,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 2,
          "mean_probability": 0.7348957494830407,
          "observed_rate": 1.0,
          "overconfidence": -0.2651042505169593,
          "observed_wilson95": [
            0.34237195288961925,
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
      "n": 2,
      "log_loss": 0.5035189055951986,
      "brier": 0.15708491661150692,
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
      "n": 2,
      "log_loss": 0.6702386177905468,
      "brier": 0.23854925967427693,
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
          "n": 1,
          "mean_probability": 0.5173743490665484,
          "observed_rate": 1.0,
          "overconfidence": -0.48262565093345156,
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
    }
  },
  "over_2_5": {
    "baseline": {
      "n": 2,
      "log_loss": 0.9712478185094237,
      "brier": 0.385793831810575,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 1,
          "mean_probability": 0.4020677237487148,
          "observed_rate": 1.0,
          "overconfidence": -0.5979322762512852,
          "observed_wilson95": [
            0.20654329147389294,
            1
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
      "n": 2,
      "log_loss": 0.7265609340960775,
      "brier": 0.26667716260888685,
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
