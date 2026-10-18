# Pinnacle totals anchoring trial

Separate proportional intensity scaling to fresh Pinnacle O/U 2.5, fitted rho and production HDA preserved. Primary Under 3.5 log loss; other markets are guardrails. No bets, automatic promotion or backfill.

Status: COLLECT_MORE_DATA; paired fixtures: 7; gameweeks: 1

{
  "under_3_5": {
    "baseline": {
      "n": 7,
      "log_loss": 0.5145539878194595,
      "brier": 0.16502690885698099,
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
      "n": 7,
      "log_loss": 0.4463287576735243,
      "brier": 0.13442423819830715,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 7,
          "mean_probability": 0.7236814569520067,
          "observed_rate": 0.8571428571428571,
          "overconfidence": -0.1334614001908504,
          "observed_wilson95": [
            0.48686549668097007,
            0.9743210440510253
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
      "n": 7,
      "log_loss": 0.6518985771017202,
      "brier": 0.22340084734299143,
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
      "n": 7,
      "log_loss": 0.5989882750024925,
      "brier": 0.2044689770347847,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 7,
          "mean_probability": 0.7492691167028965,
          "observed_rate": 0.7142857142857143,
          "overconfidence": 0.03498340241718223,
          "observed_wilson95": [
            0.35892909014821267,
            0.9177828342909844
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
      "n": 7,
      "log_loss": 0.658824733103791,
      "brier": 0.23296561163965604,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 4,
          "mean_probability": 0.4421484688492019,
          "observed_rate": 0.25,
          "overconfidence": 0.1921484688492019,
          "observed_wilson95": [
            0.045586062644636216,
            0.6993639475573634
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
      "n": 7,
      "log_loss": 0.6941002462673832,
      "brier": 0.250502702583453,
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
          "n": 6,
          "mean_probability": 0.5290298417089846,
          "observed_rate": 0.3333333333333333,
          "overconfidence": 0.19569650837565128,
          "observed_wilson95": [
            0.09676933255921683,
            0.7000116786584712
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
      "n": 7,
      "log_loss": 0.8424970834558064,
      "brier": 0.32319226099687887,
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
      "n": 7,
      "log_loss": 0.7029714047308879,
      "brier": 0.25490280298628115,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 5,
          "mean_probability": 0.48575313007963333,
          "observed_rate": 0.4,
          "overconfidence": 0.08575313007963331,
          "observed_wilson95": [
            0.1176182311592533,
            0.769280067791163
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
