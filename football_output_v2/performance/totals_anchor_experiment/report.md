# Pinnacle totals anchoring trial

Separate proportional intensity scaling to fresh Pinnacle O/U 2.5, fitted rho and production HDA preserved. Primary Under 3.5 log loss; other markets are guardrails. No bets, automatic promotion or backfill.

Status: COLLECT_MORE_DATA; paired fixtures: 8; gameweeks: 2

{
  "under_3_5": {
    "baseline": {
      "n": 8,
      "log_loss": 0.6269195743430861,
      "brier": 0.21597376492205123,
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
          "low": 0.6000000000000001,
          "high": 0.7000000000000001,
          "n": 1,
          "mean_probability": 0.6087377362101049,
          "observed_rate": 1.0,
          "overconfidence": -0.39126226378989515,
          "observed_wilson95": [
            0.20654329147389294,
            1
          ]
        },
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 4,
          "mean_probability": 0.7676242056291189,
          "observed_rate": 0.5,
          "overconfidence": 0.2676242056291189,
          "observed_wilson95": [
            0.15003570882017148,
            0.8499642911798285
          ]
        },
        {
          "low": 0.8,
          "high": 0.9,
          "n": 2,
          "mean_probability": 0.805468478186595,
          "observed_rate": 1.0,
          "overconfidence": -0.19453152181340505,
          "observed_wilson95": [
            0.34237195288961925,
            1
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.8,
        "n": 2,
        "mean_probability": 0.805468478186595,
        "observed_rate": 1.0
      }
    },
    "candidate": {
      "n": 8,
      "log_loss": 0.5521459755694741,
      "brier": 0.18341810047202928,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 8,
          "mean_probability": 0.7239109187073965,
          "observed_rate": 0.75,
          "overconfidence": -0.026089081292603455,
          "observed_wilson95": [
            0.40926987910258916,
            0.9285223111419724
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
      "n": 8,
      "log_loss": 0.6119163133718597,
      "brier": 0.20545446875359433,
      "rps": null,
      "calibration": [
        {
          "low": 0.6000000000000001,
          "high": 0.7000000000000001,
          "n": 4,
          "mean_probability": 0.6748977163999552,
          "observed_rate": 0.75,
          "overconfidence": -0.07510228360004478,
          "observed_wilson95": [
            0.3006360524426366,
            0.9544139373553637
          ]
        },
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 2,
          "mean_probability": 0.736636581800272,
          "observed_rate": 1.0,
          "overconfidence": -0.26336341819972797,
          "observed_wilson95": [
            0.34237195288961925,
            1
          ]
        },
        {
          "low": 0.8,
          "high": 0.9,
          "n": 2,
          "mean_probability": 0.8392446959290931,
          "observed_rate": 0.5,
          "overconfidence": 0.3392446959290931,
          "observed_wilson95": [
            0.09452865480086614,
            0.9054713451991339
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.78,
        "n": 2,
        "mean_probability": 0.8392446959290931,
        "observed_rate": 0.5
      }
    },
    "candidate": {
      "n": 8,
      "log_loss": 0.5608230910611952,
      "brier": 0.18700505474692566,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 8,
          "mean_probability": 0.7488010841597118,
          "observed_rate": 0.75,
          "overconfidence": -0.001198915840288195,
          "observed_wilson95": [
            0.40926987910258916,
            0.9285223111419724
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
      "n": 8,
      "log_loss": 0.6638048313598328,
      "brier": 0.23543980286022956,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 5,
          "mean_probability": 0.45316846102629765,
          "observed_rate": 0.4,
          "overconfidence": 0.05316846102629763,
          "observed_wilson95": [
            0.1176182311592533,
            0.769280067791163
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
          "n": 2,
          "mean_probability": 0.639213200156657,
          "observed_rate": 0.5,
          "overconfidence": 0.13921320015665695,
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
    },
    "candidate": {
      "n": 8,
      "log_loss": 0.687125358687751,
      "brier": 0.24701556977062275,
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
          "n": 7,
          "mean_probability": 0.5289097183825244,
          "observed_rate": 0.42857142857142855,
          "overconfidence": 0.10033828981109588,
          "observed_wilson95": [
            0.15821692226262685,
            0.7495457695909742
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
      "n": 8,
      "log_loss": 0.835073109238952,
      "brier": 0.3196514255289475,
      "rps": null,
      "calibration": [
        {
          "low": 0.30000000000000004,
          "high": 0.4,
          "n": 1,
          "mean_probability": 0.39617882318045994,
          "observed_rate": 1.0,
          "overconfidence": -0.6038211768195401,
          "observed_wilson95": [
            0.20654329147389294,
            1
          ]
        },
        {
          "low": 0.4,
          "high": 0.5,
          "n": 5,
          "mean_probability": 0.43683412739308497,
          "observed_rate": 0.6,
          "overconfidence": -0.163165872606915,
          "observed_wilson95": [
            0.23071993220883708,
            0.8823817688407467
          ]
        },
        {
          "low": 0.6000000000000001,
          "high": 0.7000000000000001,
          "n": 2,
          "mean_probability": 0.6262577108957275,
          "observed_rate": 0.0,
          "overconfidence": 0.6262577108957275,
          "observed_wilson95": [
            0,
            0.6576280471103807
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
      "n": 8,
      "log_loss": 0.7041104331979133,
      "brier": 0.2554733413818971,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 6,
          "mean_probability": 0.4865644180914648,
          "observed_rate": 0.5,
          "overconfidence": -0.013435581908535221,
          "observed_wilson95": [
            0.18761280689940868,
            0.8123871931005913
          ]
        },
        {
          "low": 0.5,
          "high": 0.6,
          "n": 2,
          "mean_probability": 0.5168129756063209,
          "observed_rate": 0.5,
          "overconfidence": 0.01681297560632089,
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
