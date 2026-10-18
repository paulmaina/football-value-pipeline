# Pinnacle totals anchoring trial

Separate proportional intensity scaling to fresh Pinnacle O/U 2.5, fitted rho and production HDA preserved. Primary Under 3.5 log loss; other markets are guardrails. No bets, automatic promotion or backfill.

Status: COLLECT_MORE_DATA; paired fixtures: 6; gameweeks: 1

{
  "under_3_5": {
    "baseline": {
      "n": 6,
      "log_loss": 0.5650775999257802,
      "brier": 0.18647922417277404,
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
          "n": 3,
          "mean_probability": 0.7712640949384348,
          "observed_rate": 0.6666666666666666,
          "overconfidence": 0.10459742827176821,
          "observed_wilson95": [
            0.2076549551264879,
            0.9385096847238394
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
      "n": 6,
      "log_loss": 0.468327161509388,
      "brier": 0.1447027374809373,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 6,
          "mean_probability": 0.7225830481006268,
          "observed_rate": 0.8333333333333334,
          "overconfidence": -0.11075028523270658,
          "observed_wilson95": [
            0.43649056343635395,
            0.9699474141282697
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
      "n": 6,
      "log_loss": 0.6914841194188727,
      "brier": 0.2414521432232065,
      "rps": null,
      "calibration": [
        {
          "low": 0.6000000000000001,
          "high": 0.7000000000000001,
          "n": 3,
          "mean_probability": 0.6796148547568164,
          "observed_rate": 0.6666666666666666,
          "overconfidence": 0.012948188090149748,
          "observed_wilson95": [
            0.2076549551264879,
            0.9385096847238394
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
      "n": 6,
      "log_loss": 0.6487501371180558,
      "brier": 0.22732456828225975,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 6,
          "mean_probability": 0.7507290881327194,
          "observed_rate": 0.6666666666666666,
          "overconfidence": 0.0840624214660528,
          "observed_wilson95": [
            0.29998832134152864,
            0.9032306674407831
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
      "n": 6,
      "log_loss": 0.6756008488736951,
      "brier": 0.24129912366960346,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 3,
          "mean_probability": 0.4469501104553582,
          "observed_rate": 0.3333333333333333,
          "overconfidence": 0.11361677712202489,
          "observed_wilson95": [
            0.0614903152761605,
            0.7923450448735121
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
      "n": 6,
      "log_loss": 0.6902853993415139,
      "brier": 0.24860001055726366,
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
          "n": 5,
          "mean_probability": 0.5324797931801374,
          "observed_rate": 0.4,
          "overconfidence": 0.13247979318013736,
          "observed_wilson95": [
            0.1176182311592533,
            0.769280067791163
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
      "n": 6,
      "log_loss": 0.8285983313703841,
      "brier": 0.316290968900403,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 4,
          "mean_probability": 0.43179647531419907,
          "observed_rate": 0.5,
          "overconfidence": -0.06820352468580093,
          "observed_wilson95": [
            0.15003570882017148,
            0.8499642911798285
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
      "n": 6,
      "log_loss": 0.7000494903544324,
      "brier": 0.25344085140759415,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 4,
          "mean_probability": 0.4855645290556369,
          "observed_rate": 0.25,
          "overconfidence": 0.2355645290556369,
          "observed_wilson95": [
            0.045586062644636216,
            0.6993639475573634
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
