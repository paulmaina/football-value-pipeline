# Pinnacle totals anchoring trial

Separate proportional intensity scaling to fresh Pinnacle O/U 2.5, fitted rho and production HDA preserved. Primary Under 3.5 log loss; other markets are guardrails. No bets, automatic promotion or backfill.

Status: COLLECT_MORE_DATA; paired fixtures: 1; gameweeks: 1

{
  "under_3_5": {
    "baseline": {
      "n": 1,
      "log_loss": 0.562443373054526,
      "brier": 0.18505905618478238,
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
        }
      ],
      "high_confidence": {
        "threshold": 0.8,
        "n": 0,
        "mean_probability": null,
        "observed_rate": null
      }
    },
    "candidate": {
      "n": 1,
      "log_loss": 0.3212489230205463,
      "brier": 0.07549157449893838,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 1,
          "mean_probability": 0.7252426989160463,
          "observed_rate": 1.0,
          "overconfidence": -0.2747573010839537,
          "observed_wilson95": [
            0.20654329147389294,
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
      "n": 1,
      "log_loss": 0.16382703501204773,
      "brier": 0.02283458351358434,
      "rps": null,
      "calibration": [
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
      "n": 1,
      "log_loss": 0.29543900947731927,
      "brier": 0.06543118292138962,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 1,
          "mean_probability": 0.744204802778884,
          "observed_rate": 1.0,
          "overconfidence": -0.255795197221116,
          "observed_wilson95": [
            0.20654329147389294,
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
      "n": 1,
      "log_loss": 0.43563688019941194,
      "brier": 0.12471310853713584,
      "rps": null,
      "calibration": [
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
      "n": 1,
      "log_loss": 0.6589885870603506,
      "brier": 0.23292751893893782,
      "rps": null,
      "calibration": [
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
      "n": 1,
      "log_loss": 1.0313608995033576,
      "brier": 0.4140646566381069,
      "rps": null,
      "calibration": [
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
      "n": 1,
      "log_loss": 0.6877698850206072,
      "brier": 0.24731137824946442,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 1,
          "mean_probability": 0.4973041104288848,
          "observed_rate": 0.0,
          "overconfidence": 0.4973041104288848,
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
