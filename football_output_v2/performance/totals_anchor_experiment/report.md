# Pinnacle totals anchoring trial

Separate proportional intensity scaling to fresh Pinnacle O/U 2.5, fitted rho and production HDA preserved. Primary Under 3.5 log loss; other markets are guardrails. No bets, automatic promotion or backfill.

Status: COLLECT_MORE_DATA; paired fixtures: 9; gameweeks: 2

{
  "under_3_5": {
    "baseline": {
      "n": 9,
      "log_loss": 0.739900613710369,
      "brier": 0.26429210301632267,
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
          "n": 3,
          "mean_probability": 0.8058942566596654,
          "observed_rate": 0.6666666666666666,
          "overconfidence": 0.13922758999299878,
          "observed_wilson95": [
            0.2076549551264879,
            0.9385096847238394
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.8,
        "n": 3,
        "mean_probability": 0.8058942566596654,
        "observed_rate": 0.6666666666666666
      }
    },
    "candidate": {
      "n": 9,
      "log_loss": 0.6279730420251222,
      "brier": 0.2188989796407851,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 9,
          "mean_probability": 0.722259244060931,
          "observed_rate": 0.6666666666666666,
          "overconfidence": 0.055592577394264375,
          "observed_wilson95": [
            0.35419734749908977,
            0.879418401317257
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
      "n": 9,
      "log_loss": 0.5892532116323659,
      "brier": 0.1950946566812686,
      "rps": null,
      "calibration": [
        {
          "low": 0.6000000000000001,
          "high": 0.7000000000000001,
          "n": 5,
          "mean_probability": 0.6729208119472545,
          "observed_rate": 0.8,
          "overconfidence": -0.12707918805274554,
          "observed_wilson95": [
            0.3755282641185388,
            0.9637768390302125
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
      "n": 9,
      "log_loss": 0.5290799613662028,
      "brier": 0.17265503214203465,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 9,
          "mean_probability": 0.749986479894905,
          "observed_rate": 0.7777777777777778,
          "overconfidence": -0.027791297882872823,
          "observed_wilson95": [
            0.4525833436728054,
            0.9367762376877727
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
      "n": 9,
      "log_loss": 0.6765245306253546,
      "brier": 0.24177659622344885,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 6,
          "mean_probability": 0.4541727462609368,
          "observed_rate": 0.5,
          "overconfidence": -0.04582725373906321,
          "observed_wilson95": [
            0.18761280689940868,
            0.8123871931005913
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
      "n": 9,
      "log_loss": 0.6749222248232318,
      "brier": 0.24094249689641004,
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
          "n": 8,
          "mean_probability": 0.5329727201667138,
          "observed_rate": 0.5,
          "overconfidence": 0.03297272016671382,
          "observed_wilson95": [
            0.21521252682444186,
            0.7847874731755582
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
      "n": 9,
      "log_loss": 0.8447241280915627,
      "brier": 0.324435198483944,
      "rps": null,
      "calibration": [
        {
          "low": 0.30000000000000004,
          "high": 0.4,
          "n": 2,
          "mean_probability": 0.39696427891117436,
          "observed_rate": 1.0,
          "overconfidence": -0.6030357210888256,
          "observed_wilson95": [
            0.34237195288961925,
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
      "n": 9,
      "log_loss": 0.7014137779854271,
      "brier": 0.2541259783950688,
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
          "n": 3,
          "mean_probability": 0.5134412456824288,
          "observed_rate": 0.6666666666666666,
          "overconfidence": -0.15322542098423786,
          "observed_wilson95": [
            0.2076549551264879,
            0.9385096847238394
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
